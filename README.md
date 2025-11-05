# SE_Assignment_lab5

NAME: SHAKTHI VELU N<BR>
SRN: PES1UG24CS830<BR>
SECTION: G<BR>

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Missing module docstring | Style | 1 | No module docstring | Add a top-level docstring |
| Missing function docstring | Style | 8, 14, 22, 25, 31, 36, 41, 48 | No docstrings for functions | Add function docstrings |
| Invalid function naming style | Style | 8, 14, 22, 25, 31, 36, 41 | Used camelCase instead of snake_case | Rename functions to snake_case |
| Dangerous default value | Bug | 8 | Mutable list used as default argument | Use `None` and initialize inside function |
| String formatting not using f-string | Style | 12 | Used `%` instead of f-string | Convert to f-string format |
| Bare except | Bug / Security | 19 | Catches all exceptions silently | Replace with specific exception type |
| Unspecified encoding | Portability | 26, 32 | `open()` call missing encoding | Add `encoding="utf-8"` |
| Global statement used | Code Smell | 27 | Uses global variable | Refactor to class or pass as param |
| File opened without context manager | Bug / Resource leak | 26, 32 | `open()` used without `with` | Use `with open(...)` |
| Use of eval() | Security | 59 | Can execute arbitrary code | Replace with safer alternative |
| Unused import | Cleanup | 2 | `logging` imported but not used | Remove import |
| Missing blank lines before function (E302) | Style | 8, 14, 22, 25, 31, 36, 41, 48 | PEP8 spacing rule violated | Add required blank lines |
| Missing blank line after function (E305) | Style | 61 | Missing blank line after function | Add required blank line |
| Try/Except/Pass | Security | 19 | Exception silently ignored | Log or handle properly |


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
