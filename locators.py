from selenium.webdriver.common.by import By


class YaMainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div.search3__input-wrapper input.search3__input')
    SUGGEST_TABLE = (By.CSS_SELECTOR, 'ul.mini-suggest__popup-content')
    OLD_MENU_BTN = (By.CSS_SELECTOR, 'a.services-pinned__all')
    MENU_BTN = (By.CSS_SELECTOR, 'div.services-suggest__icons-more')
    IMAGES_BTN = (By.CSS_SELECTOR, 'a[aria-label="Картинки"]')


class YaSearchPageLocators:
    FIRST_RESULT_LINK = (By.CSS_SELECTOR, 'ul.serp-list li.serp-item a.organic__url')
    RESULT_TABLE = (By.CSS_SELECTOR, 'ul.serp-list#search-result')


class YaImagesLocators:
    FIRST_CATEGORY_LINK = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img')
    FIRST_CATEGORY_NAME = (
    By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText')
    FIRST_CATEGORY_NAME_TEXT = ''


class YaImagesCategoryLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input.input__control')
    FIRST_PICTURE = (By.CSS_SELECTOR, 'div.serp-list div.serp-item')
    NEXT_BTN = (By.CSS_SELECTOR, 'div.CircleButton_type_next')
    PREV_BTN = (By.CSS_SELECTOR, 'div.CircleButton_type_prev')
    PIC = (By.CSS_SELECTOR, 'div.MMImageContainer')
    PIC_SRC_ATTR = (By.CSS_SELECTOR, 'img.MMImage-Origin')
    FIRST_PIC_SRC = ''
    SECOND_PIC_SRC = ''
