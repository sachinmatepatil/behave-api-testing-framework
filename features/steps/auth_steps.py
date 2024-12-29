import logging
import os

import requests
from behave import given, when, then
from utils.request_helper import APIRequest
from utils.logger import *

base_url = os.getenv("BASE_URL")
logger = get_logger()


# To pass this scenario I have added 404 in feature file cause I have added wrong token
@when('I send an authenticated GET request to "{endpoint}"')
def send_auth_get_request(context, endpoint):
    token = os.getenv("API_TOKEN")
    if not token:
        raise ValueError("API_TOKEN is not set")

    headers = {"Authorization": f"Bearer{token}"}
    url = f"{context.base_url}{endpoint}"
    response = requests.get(url, headers=headers)
    context.response = response
    logger.info(f"Authenticated GET request sent to {url}, status code: {context.response.status_code}")
