class BasePage:
    '''BasePage class pattern'''

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_current_url(self):
        '''Return current url of the page'''
        return self.browser.current_url

    def open(self):
        '''Open the url in browser'''
        self.browser.get(self.url)
