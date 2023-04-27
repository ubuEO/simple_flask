import pytest
import requests as requests

from simple_api import config


@pytest.mark.usefixtures('restart_api')
def test_api_hello_world():
    url = config.get_api_url()
    r = requests.get(f'{url}')
    assert r.status_code == 200
    assert r.text == 'Hello, World!'


@pytest.mark.usefixtures('restart_api')
def test_api_hello():
    name = 'Erentsen'
    url = config.get_api_url()
    r = requests.get(f'{url}/{name}')
    assert r.status_code == 200
    assert r.text == 'Hello, Erentsen!'

