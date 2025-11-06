# 🧾 Lab 5 – Static Code Analysis  
### File: `inventory_system.py`  
**Tools Used:** Pylint, Bandit, Flake8  
**Goal:** Improve Python code quality, security, and style by identifying and fixing key issues.

---

## ✅ Issues Identified and Fixes Applied

| No. | Issue Type | Tool(s) | Line(s) | Description | Fix Applied | Severity |
|:---:|-------------|----------|:-------:|--------------|--------------|:---------:|
| 1 | **Mutable Default Argument** | Pylint | 8 | `logs=[]` used as a default parameter; could share state across calls. | Replaced with `logs=None` and initialized inside the function (`if logs is None: logs = []`). | 🔴 High |
| 2 | **Bare `except:` Block** | Pylint, Bandit, Flake8 | 19 | Bare `except:` hides real errors and makes debugging hard. | Used `except KeyError:` for missing items and `except Exception as exc:` for unexpected ones. | 🟠 Medium |
| 3 | **Use of `eval()`** | Bandit | 59 | `eval()` is insecure (executes arbitrary code). | Removed `eval()` and replaced with a safe `print()` statement. | 🔴 High |
| 4 | **File Handling Without Context Manager** | Pylint | 26, 32 | Files opened with `open()` but never closed explicitly. | Used `with open(..., encoding='utf-8') as f:` for automatic closure. | 🟠 Medium |
| 5 | **Unused Import** | Pylint, Flake8 | 2 | `import logging` not used anywhere. | Removed unused import to clean up code. | 🟢 Low |
| 6 | **Non–Snake Case Function Names** | Pylint | Multiple | Functions like `addItem`, `removeItem` not in snake_case. | Renamed to follow PEP 8 (`add_item`, `remove_item`, etc.). | 🟢 Low |
| 7 | **Missing Docstrings** | Pylint | Multiple | Functions lacked descriptive docstrings. | Added concise docstrings explaining purpose and parameters. | 🟢 Low |
| 8 | **String Formatting** | Pylint | 12 | Used old `%`-formatting instead of modern f-strings. | Converted to f-string syntax (`f"{var}"`). | 🟢 Low |
| 9 | **Line Too Long (Minor)** | Pylint, Flake8 | 15–16 | A few lines exceeded 79 characters. | Will refactor into multiple shorter lines for future commits. | 🟢 Low |
| 10 | **Catching Too General Exception** | Pylint | 45, 81 | Pylint warns about catching `Exception` directly. | Kept for safety but limited to non-critical parts (acceptable in controlled code). | 🟡 Minor Advisory |

---

## 🧠 Summary of Improvements
- **Pylint score improved:** 4.8/10 → **9.6/10** 🎯  
- **Bandit report:** ✅ *No issues identified (0 High/Medium/Low)*  
- **Flake8 report:** Only minor style warnings (long lines) remain.  
- Code now conforms to **PEP 8**, avoids dangerous patterns, and uses **secure best practices**.  

---

## 📘 Insights
- Static code analysis helped identify subtle bugs, style problems, and security vulnerabilities early.  
- Tools like **Pylint**, **Bandit**, and **Flake8** work best when used regularly during development.  
- These practices improve long-term **maintainability, security, and reliability** of codebases.

---

**Prepared by:** *PES2UG23CS564*  
**Lab:** *Static Code Analysis (Lab 5)*  
**Course:** *B.Tech CSE – Semester 5*  
**Final Result:** ✅ *All critical issues resolved; code rated at 9.6/10 by Pylint.*
