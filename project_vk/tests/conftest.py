import pytest

from framework.browser.browser import Browser
from project_vk.tests.config_parser import ConfigParser

CONFIG = ConfigParser().get_config()
URL = CONFIG["url"]


@pytest.fixture(scope="function", autouse=True)
def set_up():
    driver = Browser().set_up_driver()
    Browser().set_url(URL)
    Browser().maximize()

    yield driver

    Browser().quit()
