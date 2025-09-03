import json

from control_up.tests.api import AIRPORT_URL, DISTANCE_URL
from core import api_command


def _get_airports_data(acc_token):
    airports = api_command.get(AIRPORT_URL, headers=api_command.get_bearer_authorization_header(acc_token))
    return json.loads(airports)["data"]


def test_airports_count(core_config):
    airports_data = _get_airports_data(core_config.ACC_TOKEN)
    assert len(airports_data) == 30


def test_airports_expected(core_config):
    expected_airports = ["Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"]
    airports_data = _get_airports_data(core_config.ACC_TOKEN)
    airports_name = [a["attributes"]["name"] for a in airports_data]
    assert set(expected_airports).issubset(airports_name)


def test_airports_distance(core_config):
    body = {"from": "KIX", "to": "NRT"}
    response = api_command.post(DISTANCE_URL,
                                headers=api_command.get_bearer_authorization_header(core_config.ACC_TOKEN), body=body)
    assert float(json.loads(response.text)["data"]["attributes"]["kilometers"]) > 400
