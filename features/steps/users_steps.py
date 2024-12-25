import os
from behave import given, when, then
from utils.logger import get_logger
from utils.request_helper import APIRequest
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# Access environment variables
base_url = os.getenv("BASE_URL")

# Access the logger
logger = get_logger()


# Step 1: Set the base URL
@given('the API base URL is SET')
def set_base_url(context):
    """
    Stores the base URL for the API in the context object.
    """
    context.base_url = base_url
    logger.info(f"Base url is set to{base_url}")


# Step 2: Send a GET request
@when('I send GET request to "{endpoint}"')
def send_get_request(context, endpoint):
    """
    Sends a GET request to the specified endpoint and stores the response.
    """
    url = f"{context.base_url}{endpoint}"  # Combine base URL and endpoint
    # response = requests.get(url)  # make the request
    context.response = APIRequest.send_get(url)  # storing response in context for further steps


@when('I send POST request to "{endpoint}" with the following data')
def send_post_request(context, endpoint):
    """
    Sends a POST request to create a new post
    """
    data = {row['key']: row['value'] for row in context.table}
    url = f"{context.base_url}{endpoint}"
    # response = requests.post(url, json=data) ///As create separate helper file
    context.response = APIRequest.send_post(url,data)


@when('I send PUT request to "{endpoint}" with the following data')
def send_put_request(context, endpoint):
    """
    Sends a PUT request to update existing record
    :param context:
    :param endpoint:
    :return:
    """
    data = {row['key']: row['value'] for row in context.table}
    url = f"{context.base_url}{endpoint}"
    # response = requests.put(url, json=data)
    context.response = APIRequest.send_put(url,data)


@when('I send a DELETE request to "{endpoint}"')
def delete_request(context, endpoint):
    """
    Sends a delete request to the endpoint
    """
    url = f"{context.base_url}{endpoint}"
    # response = requests.delete(url)
    context.response = APIRequest.send_delete(url)


# Step 3: Validate the response status code
@then('the response status code should be {status_code:d}')
def verify_status_code(context, status_code):
    """
    Verifies the status code of the response matches the expected value.
    """
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, but got {context.response.status_code}"


# Step 4: Verify the response contains a list of users
@then('the response should contain a list of users')
def verify_users_list(context):
    """
    Validates that the response contains a list of users.
    """
    json_response = context.response.json()
    assert isinstance(json_response, list), "Response is not a list"
    assert len(json_response) > 0, "User list is empty"


# To verify the response from respose data
@then('the response should contain "{key}"')
def verify_id(context, key):
    json_response = context.response.json()
    assert key in json_response, f"key '{key}' not found in response"


# To verify the response from response data title
@then('the response should contain the updated "{key}" as "{value}"')
def verify_update(context, key, value):
    """
     Validates that the response JSON contains the updated key-value pair.
    """
    json_response = context.response.json()
    assert key in json_response, f"key '{key}' not found in response"
    assert json_response[key] == value, \
        f"expected '{key}' to be '{value}', but got '{json_response[key]}"


# @then('the resource "{endpoint}" should not exist')
# def verify_deletion(context, endpoint):
#     """
#     Delete verification
#     """
#     url = f"{context.base_url}{endpoint}"
#     response = requests.get(url)
#     assert response.status_code == 404, \
#         f"expected status code 404, but got {response.status_code}"
