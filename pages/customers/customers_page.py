import allure
from data.locators import Locators
from helpers.base_page import BasePage
from helpers.help_func import StaticFunctions as Sf


class CustomersPage(BasePage):
    def __init__(self, driver):

        super().__init__(driver)

        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.locators = Locators()


    @allure.step('Открытие веб-страницы')
    def open(self, **kwargs):
        super().open(self.url)


    @allure.step('Ожидание загрузки веб-страницы')
    def wait_for_page_load(self):
        self.wait_for_specific_element(
            self.locators.CUSTOMERS_MAIN_BUTTON_LOCATOR,
            timeout=15
        )


    @allure.step('Нажатие на кнопку customers')
    def click_customers(self):
        self.click_element_by_locator(self.locators.CUSTOMERS_MAIN_BUTTON_LOCATOR)


    @allure.step('Ожидание загрузки формы')
    def wait_for_form_load(self):
        self.wait_for_specific_element(
            self.locators.HERMOINE_LABEL_LOCATOR,
            timeout=15
        )


    @allure.step('Нажатие на First Name(сортировка)')
    def click_first_name(self):
        self.click_element_by_locator(self.locators.FIRST_NAME_HYPERTEXT_LOCATOR)


    @allure.step('Удаление правильного клиента')
    def delete_close_name(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        names = Sf.chunks_to_names(customers)
        sr_ar = Sf.math_round(Sf.calc_sr_ar(names))
        del_id = Sf.calc_mid_len_name(names, sr_ar)
        del_btns = self.find_elements(self.locators.DELETE_BUTTONS_LOCATOR)
        del_btn = del_btns[del_id]
        self.click_element(del_btn)


    @allure.step('Удаление неправильного клиента')
    def delete_wrong_name(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        names = Sf.chunks_to_names(customers)
        sr_ar = Sf.math_round(Sf.calc_sr_ar(names)) - 2
        del_id = Sf.calc_mid_len_name(names, sr_ar)
        del_btns = self.find_elements(self.locators.DELETE_BUTTONS_LOCATOR)
        del_btn = del_btns[del_id]
        self.click_element(del_btn)
