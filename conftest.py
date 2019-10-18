import pytest
from selenium import webdriver
from time import sleep

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                        help='Choose language code. For example "es"')

@pytest.fixture(scope='function')
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    sleep(3)
    browser.quit()

@pytest.fixture(scope='function')    
def language(request):
    return request.config.getoption('language')
