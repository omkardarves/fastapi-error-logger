# FastAPI Error Logger

FastAPI Error Logger is a utility for logging API errors in a FastAPI application. It captures relevant information about the request, such as request body, path parameters, query parameters, headers, and more, and logs this information along with the error details.

## Installation

Install the package using pip:

```bash
pip install fastapi-error-logger
```


# Function Parameters
The log_api_error function takes the following parameters:

request: FastAPI Request object.
status_code: HTTP status code for the error.
personalized_message: Optional personalized error message.
Make sure to customize the error handling in your FastAPI application according to your requirements.


# Usage/Example

```bash
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_error_logger.api_logger import log_api_error

app = FastAPI()

@app.exception_handler(Exception)
async def handle_api_error(request: Request, exc: Exception):
    # Log API error using the log_api_error function
    await log_api_error(request, status_code=500, personalized_message="An internal server error occurred.")
    # Return a custom error response
    return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)

@app.get("/")
async def trigger_error():
    # Simulate an error for demonstration purposes
    raise ValueError("This is a simulated error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

```