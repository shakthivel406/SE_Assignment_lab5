## Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

- **Easiest fixes:** Formatting issues such as missing blank lines and removing unused imports were quick and low-risk changes. Adding encoding and replacing `%` formatting with f-strings were also straightforward.
- **Hardest fixes:** Removing `eval()`, replacing globals, and renaming functions were harder because they affected program behavior, structure, or required additional validation to avoid breaking code.

---

### 2. Did the static analysis tools report any false positives? If so, describe one example.

- No major false positives occurred, but some "missing docstring" warnings may be considered unnecessary for very small helper functions. However, technically they were valid warnings, not true false positives.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?

- **Local development:**  
  - Auto-run linters using pre-commit hooks  
  - Enable live linting in IDE (VS Code, PyCharm, etc.)  
- **CI pipeline:**  
  - Run Pylint, Bandit, and Flake8 on every pull request  
  - Fail the build on **Bandit high-severity issues**, warn on style issues  
  - Enforce minimum lint score (ex: Pylint score > 9/10)

---

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Readability improved** due to PEP8 naming, spacing, and docstrings  
- **Security improved** by removing `eval()` and bare `except`  
- **Stability improved** by replacing globals and adding type checks  
- **Maintainability improved** with class-based design and safe file handling  
- **Code became more Pythonic** (f-strings, list comprehensions, no mutable defaults)
