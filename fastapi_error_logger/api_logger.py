import json
import logging
import traceback
from datetime import datetime
from fastapi import Request
import inspect
import os


async def log_api_error(request: Request, status_code=None, personalized_message=""):
    try:
        req_body = await request.body()
        frame = inspect.currentframe().f_back
        function_name = frame.f_code.co_name
        api_title = function_name.replace("_", " ").title() + " API Error"
        
        data = {
            'req_body': req_body.decode(),
            'path_params': str(request.path_params),
            'query_params': str(request.query_params),
            'headers': {key:value for key, value in request.headers.items()},
            'api_url': str(request.base_url) + str(function_name),
            'api_title': api_title,
            'traceback': traceback.format_exc(),
            'personalized_message': personalized_message,
            'client_ip': request.client,
            'status_code': status_code,
            'req_time': str(datetime.now())
        }

        log_to_json('api_error_log.json', data)
    except Exception as e:
        logging.exception("An error occurred while logging API error: {}".format(str(e)))



def log_to_json(log_file_path, data):
    try:
        logs = []

        if os.path.exists(log_file_path):
            with open(log_file_path, "r") as f:
                logs = json.load(f)

        logs.append(data)

        with open(log_file_path, "w") as f:
            json.dump(logs, f)
    except Exception as e:
        logging.exception("An error occurred while writing to JSON file: {}".format(str(e)))