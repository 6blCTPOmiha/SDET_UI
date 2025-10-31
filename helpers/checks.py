import allure
from selenium.webdriver.common.by import By
from helpers.help_func import StaticFunctions as Sf
from data.text_data import CUSTOMERS_MAIN_DATA_CSS


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


    def new_one_customer_added(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        customer_count = len(customers) // 3
        with allure.step('Check customers count'):
            assert customer_count == 6


    def first_name_reverse_sort(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Check customers reverse sort'):
            assert names == sorted(names, reverse=True)


    def first_name_sort(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Check customers sort'):
            assert names == sorted(names)


    def delete_customer_check(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Check deleted customer in customers list'):
            assert 'Harry' not in names
