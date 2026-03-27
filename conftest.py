import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless=new")
    options.page_load_strategy = 'eager'
    options.set_capability("browserName", "chrome")
    driver = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub', options=options)
    # driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
