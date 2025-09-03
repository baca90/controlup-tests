import urllib
from urllib import parse

from core import core_test_config

AIRPORT_URL = urllib.parse.urljoin(core_test_config.API_URL, "airports/")
DISTANCE_URL = urllib.parse.urljoin(AIRPORT_URL, "distance")
