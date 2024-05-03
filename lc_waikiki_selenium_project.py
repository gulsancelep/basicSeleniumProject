from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LcWaikikiSeleniumProject(unittest.TestCase):
    baseUrl = "https://www.lcwaikiki.com/tr-TR/TR"
    MENU = (By.LINK_TEXT, "KADIN")
    SUB_MENU = (By.LINK_TEXT, "Bluz")
    PRODUCT = (By.CLASS_NAME, "product-image")
    SIZE = (By.LINK_TEXT, "48")
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "SEPETE EKLE")
    CART_ITEM_COUNT = (By.XPATH, "//span[@class = 'badge-circle']")
    HOME_PAGE_LOGO = (By.CLASS_NAME, "main-header-logo")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(15)

    def lc_waikiki_selenium_test_case(self):
        assert self.baseUrl == self.driver.current_url
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.MENU)).perform()
        self.driver.find_element(*self.SUB_MENU).click()
        assert "bluz" in self.driver.current_url
        self.driver.find_elements(*self.PRODUCT)[3].click()
        assert "urun" in self.driver.current_url
        self.driver.find_element(*self.SIZE).click()
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        self.driver.find_element(*self.CART_ITEM_COUNT).click()
        assert "sepetim" in self.driver.current_url
        self.driver.find_element(*self.HOME_PAGE_LOGO).click()
        assert self.baseUrl == self.driver.current_url

    def tearDown(self):
        self.driver.close()
