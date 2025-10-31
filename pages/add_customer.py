from helpers.help_func import StaticFunctions as Sf
from data.text_data import URL
from data.text_data import LAST_NAME
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.post_code = Sf.post_code_gen()


    def open(self):
        self.driver.get(URL)


    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
        ), message='Страница не загружается')


    def click_add_customer(self):
        add_customer_button = self.driver.find_element(By.CSS_SELECTOR, '[ng-class="btnClass1"]')
        add_customer_button.click()

    def wait_for_form_load(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[type = "submit"]'),
        ), message='Форма не загружается')


    def input_first_name(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="fName"]')
        post_code_value = self.post_code
        first_name_value = Sf.first_name_calc(post_code_value)
        first_name.send_keys(first_name_value)


    def input_last_name(self):
        last_name = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="lName"]')
        last_name.send_keys(LAST_NAME)


    def input_post_code(self):
        post_code = self.driver.find_element(By.CSS_SELECTOR, '[ng-model="postCd"]')
        post_code_value = self.post_code
        post_code.send_keys(post_code_value)


    def click_add_customer_button(self):
        add_customer_button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        add_customer_button.click()


    def ok_alert_message(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.switch_to.default_content()
