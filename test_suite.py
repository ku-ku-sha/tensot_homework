from pages.ya_main_page import YaMainPage
from pages.ya_search_page import YaSearchPage
from pages.ya_images_page import YaImagesPage
from pages.ya_images_category_page import YaImagesCategoryPage
from pages.constants import Constants as Const
from pages.locators import YaImagesCategoryLocators as YICL


def test_yandex_search(browser):
    '''Test scenario "Yandex Search"'''
    page = YaMainPage(browser, Const.URL_YANDEX)
    page.open()  # go to the main yandex page
    page.search_field.is_present()  # check the search field is present
    page.search_field.send_keys_to(Const.SEARCH_REQUEST)  # enter "Tensor" in the search field
    page.suggest_table.is_present()  # check the suggest table is present
    page.search_field.press_enter()  # press Enter
    page = YaSearchPage(browser, page.get_current_url())
    page.search_page_is_present()  # check the search page is present
    page.first_result_link_is_for_tensor()  # check that first link in search results is for Tensor


def test_yandex_pictures(browser):
    '''Test scenario "Yandex Images"'''
    page = YaMainPage(browser, Const.URL_YANDEX)
    page.open()  # go to the main yandex page
    page.no_old_menu_btn()  # check the old menu button is not present
    page.menu_btn_is_present()  # check the new menu button is present
    page.menu_btn.click_on()  # open the menu
    page.open_images()  # select Yandex Images
    page = YaImagesPage(browser, page.get_current_url())
    page.ya_images_page_is_open()  # check the current url equals Yandex Images url
    page.go_to_first_category()  # go to the first category
    page = YaImagesCategoryPage(browser, page.get_current_url())
    page.category_name_is_in_search_field()  # check that category name is in the search field
    page.first_picture.click_on()  # open the first image
    page.pic.is_present()  # check that the image is present
    YICL.FIRST_PIC_SRC = page.pic_src.get_element_attribute('src')
    page.next_btn.click_on()  # press the next button
    YICL.SECOND_PIC_SRC = page.pic_src.get_element_attribute('src')
    page.picture_is_the_same(YICL.FIRST_PIC_SRC, YICL.SECOND_PIC_SRC,
                             param='not')  # compare the picture's id before and after clicking the next button, check the picture has changed
    page.prev_btn.click_on()  # press the previous button
    YICL.SECOND_PIC_SRC = page.pic_src.get_element_attribute('src')
    page.picture_is_the_same(YICL.FIRST_PIC_SRC,
                             YICL.SECOND_PIC_SRC)  ##compare first picture id and id after clicking the previos button, check it matched
