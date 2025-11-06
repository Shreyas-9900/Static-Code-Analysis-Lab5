### Reflection

1. **Easiest vs Hardest Fixes:**
   - Easiest: Removing unused imports and fixing style warnings.
   - Hardest: Replacing `eval()` and fixing mutable default arguments since they required logic changes.

2. **False Positives:**
   - Bandit flagged a simple try/except block as risky, but I modified it to catch specific errors for safety.

3. **Integration in Workflow:**
   - I would integrate Pylint, Bandit, and Flake8 in a CI pipeline (e.g., GitHub Actions) so every push automatically checks code quality.

4. **Tangible Improvements:**
   - My code became cleaner, more secure, and more maintainable.  
     Pylint score improved from **4.8/10 → 9.x/10**.
