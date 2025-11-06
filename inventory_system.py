"""inventory_system.py

Simple inventory utilities for a minimal inventory system used in the lab.
Provides functions to add/remove items, persist/load JSON, and report low stock.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

# Global variable holding inventory: item -> quantity
stock_data: Dict[str, int] = {}


def add_item(item: str = "default", qty: int = 0, logs: Optional[List[str]] = None) -> None:
    """Add qty of item to the inventory. `logs` if provided will be appended with an action entry."""
    if logs is None:
        logs = []

    # validate types
    if not isinstance(item, str):
        raise TypeError("item must be a string")
    if not isinstance(qty, int):
        raise TypeError("qty must be an integer")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int) -> None:
    """Remove qty of item from the inventory. Ignores missing items."""
    try:
        if not isinstance(item, str):
            raise TypeError("item must be a string")
        if not isinstance(qty, int):
            raise TypeError("qty must be an integer")

        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
    except KeyError:
        # item not present: nothing to remove
        pass
    except Exception as exc:  # keep broad handler only for unexpected errors
        print(f"Unexpected error removing item: {exc}")


def get_qty(item: str) -> int:
    """Return quantity for item (0 if not present)."""
    if not isinstance(item, str):
        raise TypeError("item must be a string")
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> None:
    """Load inventory from a JSON file into the module's stock_data."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            # update existing global dict without reassigning the variable
            stock_data.clear()
            for k, v in data.items():
                # Ensure quantities are ints
                stock_data[str(k)] = int(v)
        else:
            print("Warning: inventory file did not contain a JSON object.")
    except FileNotFoundError:
        # File doesn't exist yet — this is fine for many workflows
        pass
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"Error loading inventory file: {exc}")


def save_data(file: str = "inventory.json") -> None:
    """Save the current inventory to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)
    except Exception as exc:
        print(f"Error saving inventory file: {exc}")


def print_data() -> None:
    """Print a simple inventory report to stdout."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold: int = 5) -> List[str]:
    """Return a list of items with quantity below threshold."""
    if not isinstance(threshold, int):
        raise TypeError("threshold must be an integer")

    result: List[str] = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main() -> None:
    """Example usage of the inventory utilities."""
    # Example run: valid calls
    add_item("apple", 10)
    add_item("banana", 2)  # positive restock
    # invalid type calls are now prevented by type checks (would raise)
    remove_item("apple", 3)
    remove_item("orange", 1)  # orange not present — safe

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()

    # Removed insecure eval usage. Use direct logging/printing instead.
    print("eval removed for safety")


if __name__ == "__main__":
    main()
