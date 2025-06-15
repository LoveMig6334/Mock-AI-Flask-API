# Troubleshooting Guide

## Import Errors

If you encounter ModuleNotFoundError issues like:
```
ModuleNotFoundError: No module named 'src'
```

There are two ways to fix this:

### 1. Use Relative Imports (Used inside the src directory)

Inside the `src` directory, use relative imports like this:
```python
# Instead of
from src.logger import setup_logger

# Use this
from logger import setup_logger
```

This has been implemented in the current code for all files within the `src` directory.

### 2. Add the src Directory to Python Path (Used for example_logging.py)

For scripts outside the `src` directory that need to import from it:

```python
import os
import sys

# Add src directory to Python path
src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_dir)

# Now import directly from the modules
from log_utils import log_error
from logger import setup_logger
```

This approach is used in the `example_logging.py` script.

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
