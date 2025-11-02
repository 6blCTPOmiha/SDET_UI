import allure
from helpers.help_func import StaticFunctions as Sf
from data.text_data import LAST_NAME, POST_CODE_1
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.post_code_2 = Sf.post_code_gen()
        self.post_code_1 = POST_CODE_1
        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'


    with allure.step('Открытие веб-страницы'):
        def open(self):
            self.driver.get(self.url)


    with allure.step('Ожидание загрузки страницы'):
        def wait_for_page_load(self):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
            ), message='Страница не загружается')


    with allure.step('Нажатие на кнопку add_customer'):
        def click_add_customer(self):
            add_customer_button = self.driver.find_element(By.CSS_SELECTOR, '[ng-class="btnClass1"]')
            add_customer_button.click()


    with allure.step('Ожидание загрузки формы'):
        def wait_for_form_load(self):
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[type = "submit"]'),
            ), message='Форма не загружается')


    with allure.step('Ввод имени'):
        def input_first_name(self):
            first_name = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="fName"]')
            post_code_value = self.post_code_1
            first_name_value = Sf.first_name_calc(post_code_value)
            first_name.send_keys(first_name_value)


    with allure.step('Ввод фамилии'):
        def input_last_name(self):
            last_name = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="lName"]')
            last_name.send_keys(LAST_NAME)


    with allure.step('Ввод кода'):
        def input_post_code(self):
            post_code = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="postCd"]')
            post_code_value = self.post_code_1
            post_code.send_keys(post_code_value)


    with allure.step('Нажатие на кнопку add_customer'):
        def click_add_customer_button(self):
            add_customer_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
            add_customer_button.click()


    with allure.step('Нажатие ок на алерте'):
        def ok_alert_message(self):
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.switch_to.default_content()
