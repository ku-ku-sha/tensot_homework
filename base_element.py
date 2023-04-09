from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from termcolor import cprint


class BaseElement(object):
    '''BaseElement class pattern'''

    def __init__(self, locator, browser, timeout=10):
        self.locator = locator
        self.browser = browser

    def find_element(self, timeout=10):
        '''Find the element on the page'''
        element = None
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            assert False, '\nNo such element on page, Error: TimeoutException'
        return element

    def is_present(self, timeout=15) -> bool:
        '''Checks the element is present on page'''
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(self.locator) and EC.element_to_be_clickable(self.locator))
        except TimeoutException:
            assert False, '\nNo such element on page, Error: TimeoutException'
        return True

    def click_on(self):
        '''Click on element'''
        try:
            element = self.find_element()
            element.click()
        except:
            assert False, "\nThe element isn't clickable."

    def send_keys_to(self, text):
        '''Input the text in the editable text field'''
        element = self.find_element()
        try:
            element.click()
            element.clear()
            element.send_keys(text)
        except Exception as error:
            assert False, f"\nUnable to send keys. Error: {error}"

    def press_enter(self):
        '''Imitating typing Enter on a keyboard'''
        try:
            element = self.find_element()
            element.send_keys(Keys.ENTER)
        except Exception:
            assert False, '\nThe error occurred when press_enter() function calling.'

    def get_text(self) -> str:
        '''Return visible text from the element'''
        element = self.find_element()
        try:
            text = str(element.text)
        except Exception as error:
            assert False, f'\nget_text Error: {error}'
        return text

    def get_element_attribute(self, attribute) -> str:
        '''Return the value of given attribute of the element'''
        element = self.find_element()
        attribute_value = ''
        try:
            attribute_value = element.get_attribute(attribute)
        except Exception as error:
            assert False, f'\n get_element_attribute Error: {error}'
        return attribute_value
