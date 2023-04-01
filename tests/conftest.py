import pytest
from selene.support.shared import browser
from utils.base_session import demowebshop
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope='session')
def register():
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demowebshop.post('/login', data={'Email': os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD')}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    return browser
