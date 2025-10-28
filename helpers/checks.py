import re
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Checks:
    def __init__(self, driver):
        self.driver = driver


    def add_customer_form_loaded(self):
        customer = self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]')
        with allure.step('Check if add_customer form is loaded'):
            assert customer != ''


    def customers_form_loaded(self):
        customer = self.driver.find_element(By.XPATH, '//td[contains(text(), "Hermoine")]')
        with allure.step('Check if customers form is loaded'):
            assert customer != ''
