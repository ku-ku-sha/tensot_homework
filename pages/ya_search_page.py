import time

from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.locators import YaSearchPageLocators as YSL
from termcolor import cprint
from pages.constants import Constants as Const


class YaSearchPage(BasePage):
    '''Yandex Search Page'''

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # page elements definition
        self.search_results = BaseElement(YSL.RESULT_TABLE, browser)
        self.first_result_link = BaseElement(YSL.FIRST_RESULT_LINK, browser)

    def search_page_is_present(self):
        '''The function checks search results are present on a page and the current url contains "search"'''
        current_url = ''
        try:
            self.search_results.is_present()
            current_url = self.get_current_url()
            assert 'search' in current_url, 'No "search" in current url'
        except (Exception and not AssertionError) as error:
            return False, 'No search results. Error: {error}'
        return True

    def first_result_link_is_for_tensor(self):
        '''The function checks the first link in search result is for tensor.ru'''
        try:
            href_attribute = self.first_result_link.get_element_attribute('href')
            assert Const.URL_TENSOR == href_attribute, f'\nExpected first link is for tensor, got {href_attribute}'
        except AttributeError as error:
            assert False, f'first_result_link_is_for_tensor Error: {error}'
