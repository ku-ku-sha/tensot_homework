from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.locators import YaImagesLocators as YIL
from pages.constants import Constants as Const


class YaImagesPage(BasePage):
    '''Yandex Images Page'''
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.first_category_link = BaseElement(YIL.FIRST_CATEGORY_LINK, browser)
        self.first_category_name = BaseElement(YIL.FIRST_CATEGORY_NAME, browser)

    def ya_images_page_is_open(self):
        '''The function checks that the current url is equal to url of yandex images.'''
        current_url = self.get_current_url()
        expected_url = Const.URL_YANDEX_IMAGES
        assert current_url == expected_url, f'Expected {expected_url}, got {current_url}.'

    def go_to_first_category(self):
        '''The function opens the first category in Yandex images'''
        try:
            YIL.FIRST_CATEGORY_NAME = self.first_category_name.get_text()
            self.browser.execute_script("arguments[0].click();", self.first_category_link.find_element())
        except Exception as error:
            assert False, f'Unable to go to the first category. Error: {error}'

