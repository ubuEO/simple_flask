import time
from pathlib import Path

import pytest
import requests

from simple_api import config


@pytest.fixture
def restart_api():
    (Path(__file__).parent / "../src/simple_api/main.py").touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()

def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    url = config.get_api_url()
    while time.time() < deadline:
        try:
            return requests.get(url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")
