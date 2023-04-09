from selenium import webdriver
import pytest



@pytest.fixture(scope='function')
def browser():
    '''browser start and teardown methods wrapped in pytest fixture'''
    browser = webdriver.Chrome()
    browser.delete_all_cookies()
    yield browser
    browser.quit()


