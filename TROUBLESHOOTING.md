# Troubleshooting Guide

## Import Errors

If you encounter ModuleNotFoundError issues like:
```
ModuleNotFoundError: No module named 'src'
```

There are two ways to fix this:

### 1. Use Relative Imports (Recommended for this project)

Inside the `src` directory, use relative imports like this:
```python
# Instead of
from src.logger import setup_logger

# Use this
from logger import setup_logger
```

This has been fixed in the current code.

### 2. Add the Project Root to Python Path

If you're importing modules from outside the `src` directory:

```python
import os
import sys

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Then import using src.
from src.logger import setup_logger
```

## Error Handling and Logging

The example script demonstrates two approaches to error handling:

1. **Catch and Continue**: In the `main()` function, we catch the exception and continue execution.
2. **Proper Error Handling**: In the `proper_error_handling()` function, we catch the exception and return a value indicating failure.

Best practices:
- Always log exceptions
- Use `try`/`except`/`finally` blocks appropriately
- Return meaningful values to indicate success/failure
- Use context in log_error to provide additional information

## Running the Application

From the project root:

```powershell
cd "c:\Users\thatt\Documents\Coding Project\Python Projects\PyFlask-API Mock"
python src/app.py
```

From inside the src directory:

```powershell
cd "c:\Users\thatt\Documents\Coding Project\Python Projects\PyFlask-API Mock\src"
python app.py
```
