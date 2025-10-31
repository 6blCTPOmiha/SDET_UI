import re
import allure
from selenium.webdriver.common.by import By
from helpers.help_func import StaticFunctions as Sf
from selenium.webdriver.support.ui import Select
from data.text_data import CUSTOMERS_MAIN_DATA_CSS


class Checks:
    def __init__(self, driver):
        self.driver = driver


    def add_customer_form_loaded(self):
        customer = self.driver.find_element(By.CSS_SELECTOR, '[type = "submit"]')
        with allure.step('Проверка загрузки формы add_customer'):
            assert customer != '', 'Форма add customer не загружается'


    def customers_form_loaded(self):
        customer = self.driver.find_element(By.XPATH, '//td[contains(text(), "Hermoine")]')
        with allure.step('Проверка загрузки формы customers'):
            assert customer != '', 'Форма customers не загружается'


    def new_one_customer_added(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        customer_count = len(customers) // 3
        with allure.step('Проверка количества клиентов'):
            assert customer_count == 6, 'Количество пользователей некорректное'


    def first_name_reverse_sort(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Проверка обратной сортировки клиентов'):
            assert names == sorted(names, reverse=True), 'Сортировка выполнена некорректно'


    def first_name_sort(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Проверка сортировки клиентов'):
            assert names == sorted(names), 'Сортировка выполнена некорректно'


    def delete_customer_check(self):
        customers = self.driver.find_elements(By.CSS_SELECTOR, CUSTOMERS_MAIN_DATA_CSS)
        names = Sf.chunks_to_names(customers)
        with allure.step('Проверка удаления клиента из списка'):
            assert 'Harry' not in names, 'удалён некорректный клиент'
