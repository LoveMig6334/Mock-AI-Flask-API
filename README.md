# PyFlask-API Mock with React Frontend

This project demonstrates a full-stack application with a Flask API backend and a React frontend, featuring a robust logging system.

## Features

- **Backend**:
  - Flask API with RESTful endpoints
  - Comprehensive logging system with:
    - Request/response logging
    - Error tracking
    - Detailed context logging
    - Log rotation and management
    - Configurable logging options

- **Frontend**:
  - Modern React application
  - API integration with the Flask backend
  - Interactive UI for testing the API

## Project Structure

```
PyFlask-API Mock/
|-- logs/                  # Log files directory
|-- resources/             # Resource files
|-- src/
|   |-- backend/           # Flask backend
|   |   |-- app.py         # Main Flask application
|   |   |-- config.py      # Configuration settings
|   |   |-- logger.py      # Logger setup and configuration
|   |   |-- log_utils.py   # Logging utility functions
|   |-- frontend/          # React frontend
|       |-- public/        # Static assets
|       |-- src/           # React source code
|           |-- App.js     # Main React component
|           |-- index.js   # Entry point
|-- example_logging.py     # Example script showing logging usage
|-- GIL-TEST.py            # Python GIL test file
|-- README.md              # This readme file
|-- TROUBLESHOOTING.md     # Troubleshooting guide
```

## Import Structure

The project uses a structured import approach:

- Files within `src/backend/` use relative imports (e.g., `from logger import setup_logger`)
- External scripts like `example_logging.py` add the `src/backend` directory to the Python path

See `TROUBLESHOOTING.md` for more details on handling import issues.

## Getting Started

### Prerequisites

- **Backend**:
  - Python 3.6+
  - Flask
  - Flask-CORS

- **Frontend**:
  - Node.js 16+
  - npm or yarn

### Installation

#### Backend Setup
1. Clone the repository
2. Install required packages:

```powershell
pip install flask flask-cors
```

#### Frontend Setup
1. Navigate to the frontend directory:

```powershell
cd src/frontend
```

2. Install dependencies:

```powershell
npm install
```

### Running the Application

#### Running the Backend

```powershell
python src/backend/app.py
```

The API server will start on port 5000.

#### Running the Frontend

```powershell
cd src/frontend
npm start
```

The React development server will start on port 3000 and open in your browser automatically.

## API Endpoints

### Message Endpoint

- **URL**: `/api/message`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "Hello from Flask!"
  }
  ```

### Echo Endpoint

- **URL**: `/api/echo`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "text": "Your message here"
  }
  ```
- **Response**:
  ```json
  {
    "you_sent": {
      "text": "Your message here"
    }
  }
  ```

## Logging System

### Log Files

Logs are stored in the `log/` directory with filenames in the format `api_YYYY-MM-DD.log`. The logs will rotate automatically when they reach the configured size limit.

### Log Structure

Each log entry includes:
- Timestamp
- Log level (INFO, ERROR, etc.)
- Module name
- Message

Additionally, detailed logs include:
- Request ID (for tracing requests)
- Request/response details
- Error context and stack traces

### Configuration

Logging behavior can be customized through environment variables:

| Environment Variable | Description | Default |
|----------------------|-------------|---------|
| LOG_LEVEL | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) | INFO |
| MAX_LOG_SIZE | Maximum log file size in bytes before rotation | 10485760 (10MB) |
| BACKUP_COUNT | Number of backup log files to keep | 10 |
| INCLUDE_STACK_TRACE | Whether to include stack traces in error logs | True |
| LOG_DETAILED_REQUESTS | Whether to log detailed request and response data | True |
| LOG_FORMAT | Format string for log messages | %(asctime)s - %(name)s - %(levelname)s - %(message)s |
| DATE_FORMAT | Date format for timestamps | %Y-%m-%d %H:%M:%S |

## Using the Logging System in Your Code

### Basic Logging

```python
from logger import setup_logger

# Get logger instance
logger = setup_logger('my_module')

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Advanced Logging

```python
from log_utils import log_error

# Log an error with context
try:
    # Some code that might raise an exception
    result = 10 / 0
except Exception as e:
    log_error(e, request, {"operation": "division", "value": 0})
```

### Logging API Requests and Responses

```python
from log_utils import log_api_request, log_api_response

# In your Flask route handler
@app.route("/api/data", methods=["POST"])
def handle_data():
    # Log the incoming request
    log_api_request(request)
    
    # Process the request...
    result = {"status": "success"}
    
    # Create response
    response = jsonify(result)
    
    # Log the response
    log_api_response(request, response, result)
    
    return response
```

## Extending the Logging System

To add custom logging functionality:

1. Create a new utility function in `log_utils.py`
2. Import and use it in your application code

Example:

```python
# In log_utils.py
def log_custom_event(event_type, event_data):
    logger = setup_logger('custom_events')
    logger.info(f"Custom event: {event_type} - {json.dumps(event_data)}")

# In your application code
from log_utils import log_custom_event

log_custom_event("user_login", {"user_id": "123", "ip": "192.168.1.1"})
```

## Frontend Application

The project includes a React frontend that interacts with the Flask backend API.

### Features
- Simple, responsive UI
- API integration with the Flask backend
- Real-time data fetching and display

### Component Structure
- `App.js`: Main application component
  - Fetches data from the `/api/message` endpoint on load
  - Provides a form to send data to the `/api/echo` endpoint
  - Displays the response from the backend

### Development

The frontend is built with React 19 and uses standard create-react-app tooling. To make changes to the frontend:

1. Navigate to the frontend directory:

```powershell
cd src/frontend
```

2. Run the development server:

```powershell
npm start
```

3. Make changes to the files in `src/frontend/src/`
4. The browser will automatically reload with your changes

### Building for Production

To create a production build of the frontend:

```powershell
cd src/frontend
npm run build
```

This will create optimized static files in the `build` directory that can be served by any static file server or integrated with the Flask backend.

## Deployment

### Development Environment
For local development, run both the backend and frontend servers as described in the "Running the Application" section.

### Production Environment
For production deployment:

1. Build the React frontend:
```powershell
cd src/frontend
npm run build
```

2. Serve the Flask backend using a production-grade WSGI server like Gunicorn:
```powershell
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 'src.backend.app:app'
```

3. Consider using Nginx or another web server to:
   - Serve static files from the React build
   - Proxy API requests to the Flask application
   - Handle HTTPS

### Environment Variables
Configure the application behavior using environment variables:

```powershell
# Set log level to DEBUG
$env:LOG_LEVEL = "DEBUG"

# Start the Flask application
python src/backend/app.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the MIT License.

---

**Last Updated:** June 19, 2025
