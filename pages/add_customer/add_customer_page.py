import allure
from helpers.base_page import BasePage
from helpers.help_func import StaticFunctions as Sf
from data.text_data import LAST_NAME, POST_CODE_1
from data.locators import Locators


class AddCustomerPage(BasePage):
    def __init__(self, driver):

        super().__init__(driver)

        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.locators = Locators()
        self.post_code_2 = Sf.post_code_gen()
        self.post_code_1 = POST_CODE_1


    @allure.step('Открытие веб-страницы')
    def open(self, **kwargs):
        super().open(self.url)


    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self):
        self.wait_for_specific_element(
            self.locators.ADD_CUSTOMER_MAIN_BUTTON_LOCATOR,
            timeout=15
        )


    @allure.step('Нажатие на кнопку add_customer')
    def click_add_customer(self):
        self.click_element_by_locator(self.locators.ADD_CUSTOMER_MAIN_BUTTON_LOCATOR)


    @allure.step('Ожидание загрузки формы')
    def wait_for_form_load(self):
        self.wait_for_specific_element(
            self.locators.SUBMIT_BUTTON_LOCATOR,
            timeout=15
        )


    @allure.step('Ввод имени')
    def input_first_name(self):
        first_name = self.find_element(self.locators.FIRST_NAME_TEXT_BOX_LOCATOR)
        post_code_value = self.post_code_1
        first_name_value = Sf.first_name_calc(post_code_value)
        first_name.send_keys(first_name_value)


    @allure.step('Ввод фамилии')
    def input_last_name(self):
        last_name = self.find_element(self.locators.LAST_NAME_TEXT_BOX_LOCATOR)
        last_name.send_keys(LAST_NAME)


    @allure.step('Ввод кода')
    def input_post_code(self):
        post_code = self.find_element(self.locators.POST_CODE_TEXT_BOX_LOCATOR)
        post_code_value = self.post_code_1
        post_code.send_keys(post_code_value)


    @allure.step('Нажатие на кнопку подтверждения введённых данных (add_customer)')
    def click_add_customer_button(self):
        add_customer_button = self.find_element(self.locators.SUBMIT_BUTTON_LOCATOR)
        add_customer_button.click()


    @allure.step('Нажатие ок на алерте')
    def click_ok_alert_message(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.switch_to.default_content()
