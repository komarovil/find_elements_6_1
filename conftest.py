import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions


def pytest_addoption(parser):
    parser.addoption("--chrome", action="store", default=None, help="chrome")
    parser.addoption("--firefox", action="store", default=None, help="firefox")


@pytest.fixture()
def url():
    return 'http://192.168.43.80/opencart/'


@pytest.fixture()
def chrome(request):
    return request.config.getoption("--chrome")



@pytest.fixture
def chrome_browser(request):
    options = ChromeOptions()
    options.add_argument("--start-fullscreen")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture()
def chrome(request):
    return request.config.getoption("--firefox")


@pytest.fixture
def firefox_browser(request):
    options_2 = FirefoxOptions()
    options_2.add_argument("--start-fullscreen")
    wd2 = webdriver.Firefox()
    request.addfinalizer(wd2.quit)
    return wd2