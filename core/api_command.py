import requests
from requests import PreparedRequest

from core.core_logger import LOGGER

req = PreparedRequest()
session = requests.session()


# region headers


def get_bearer_authorization_header(token):
    return {"Authorization": f"Bearer {token}"}


# endregion


# region calls


def get(api_url, headers):
    response = session.get(api_url, headers=headers, verify=False)
    LOGGER.test_info(f"GET {api_url} response: code {response.status_code}")
    return response.text


def post(api_url, headers, body=None, verify=False):
    response = requests.post(api_url, headers=headers, json=body, verify=verify)
    LOGGER.test_info(f"POST {api_url} response: code {response.status_code}, message {response.text}")
    return response

# endregion
