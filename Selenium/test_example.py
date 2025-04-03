import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Or any other browser driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
