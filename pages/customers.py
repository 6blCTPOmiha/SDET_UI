import allure
from helpers.help_func import StaticFunctions as Sf
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Customers:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.customers_main_data_css = '[class="ng-binding"]'


    with allure.step('Открытие веб-страницы'):
        def open(self):
            self.driver.get(self.url)


    with allure.step('Ожидание загрузки веб-страницы'):
        def wait_for_page_load(self):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
            ), message='Страница не загружается')


    with allure.step('Нажатие на кнопку customers'):
        def click_customers(self):
            customers_button = self.driver.find_element(By.CSS_SELECTOR, '[ng-class="btnClass3"]')
            customers_button.click()


    with allure.step('Ожидание загрузки формы'):
        def wait_for_form_load(self):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//td[contains(text(), "Hermoine")]')
            ), message='Форма не загружается')


    with allure.step('Нажатие на First Name(сортировка)'):
        def click_first_name(self):
            first_name = self.driver.find_element(By.XPATH, '//a[contains(text(), "First Name")]')
            first_name.click()


    with allure.step('Удаление правильного клиента'):
        def delete_close_name(self):
            customers = self.driver.find_elements(By.CSS_SELECTOR, self.customers_main_data_css)
            names = Sf.chunks_to_names(customers)
            sr_ar = Sf.math_round(Sf.calc_sr_ar(names))
            del_id = Sf.calc_mid_len_name(names, sr_ar)
            del_btns = self.driver.find_elements(By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')
            del_btns[del_id].click()


    with allure.step('Удаление неправильного клиента'):
        def delete_wrong_name(self):
            customers = self.driver.find_elements(By.CSS_SELECTOR, self.customers_main_data_css)
            names = Sf.chunks_to_names(customers)
            wrong_sr_ar = Sf.math_round(Sf.calc_sr_ar(names)) - 2
            del_id = Sf.calc_mid_len_name(names, wrong_sr_ar)
            del_btns = self.driver.find_elements(By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')
            del_btns[del_id].click()
