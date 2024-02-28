import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_one(browser):
    browser.get('https://sbis.ru/download?tab=plugin&innerTab=default')
    browser.find_element(By.CLASS_NAME, 'controls-TabButton__inner').click()
