from pages.base_page import BasePage
from pages.base_element import BaseElement
from pages.locators import YaImagesCategoryLocators as YICL
from pages.locators import YaImagesLocators as YIL


class YaImagesCategoryPage(BasePage):
    '''Yandex Images Category Page'''

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.search_field = BaseElement(YICL.SEARCH_FIELD, browser)
        self.first_picture = BaseElement(YICL.FIRST_PICTURE, browser)
        self.next_btn = BaseElement(YICL.NEXT_BTN, browser)
        self.prev_btn = BaseElement(YICL.PREV_BTN, browser)
        self.pic = BaseElement(YICL.PIC, browser)
        self.pic_src = BaseElement(YICL.PIC_SRC_ATTR, browser)

    def category_name_is_in_search_field(self):
        '''The function check the category name is in search field'''
        try:
            category_name = YIL.FIRST_CATEGORY_NAME_TEXT
            search_field_text = self.search_field.get_text()
            assert category_name == search_field_text, '\nNo category name in search field.'
        except (Exception and not AssertionError) as error:
            assert False, f'category_name_is_in_search_field Error: {error}'
        return True

    def picture_is_the_same(self, id_1, id_2, param=''):
        '''picture_is_the_same function calling without a parameter param checks the equalty of the id_1 and id_2.
            The function calling with the parameter param="not" checks that id_1 != id_2'''
        if param == 'not':
            assert id_1 != id_2, f'Error: Images match '
        elif not param:
            assert id_1 == id_2, f'Error: Images differ'
        else:
            assert False, 'picture_is_the_same Error: parameter is invalid'
