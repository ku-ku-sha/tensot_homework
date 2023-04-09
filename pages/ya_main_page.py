from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.locators import YaMainPageLocators as YL
from selenium.common import exceptions
from termcolor import cprint


class YaMainPage(BasePage):
    '''Yandex main page'''

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # page elements definition
        self.search_field = BaseElement(YL.SEARCH_FIELD, browser)
        self.suggest_table = BaseElement(YL.SUGGEST_TABLE, browser)
        self.old_menu_btn = BaseElement(YL.OLD_MENU_BTN, browser)
        self.menu_btn = BaseElement(YL.MENU_BTN, browser)
        self.images_btn = BaseElement(YL.IMAGES_BTN, browser)

    def no_old_menu_btn(self):
        '''The function check the absence of the old menu button '''
        try:
            self.old_menu_btn.is_present()
        except TimeoutError:
            assert True
        assert False, f'The old menu button is visible'

    def menu_btn_is_present(self):
        '''The function checks the menu button is present on a page after clicking on the search field'''
        try:
            self.search_field.click_on()
            self.menu_btn.is_present()
        except (Exception and not AssertionError) as error:
            assert False, f"\nThe menu button isn't present. Error: {error}"
        return True

    def open_images(self):
        '''the function opens Yandex Images and switches to a new tab in browser'''
        try:
            self.images_btn.click_on()
            new_tab = self.browser.window_handles[1]
            self.browser.switch_to.window(new_tab)
        except (Exception and not AssertionError) as error:
            assert False, f'Unable to open Yandex Images. Error: {error}'
        return True
