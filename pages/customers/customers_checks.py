import allure
from helpers.base_page import BasePage
from helpers.help_func import StaticFunctions as Sf
from data.locators import Locators


class CustomersChecks(BasePage):
    def __init__(self, driver):

        super().__init__(driver)

        self.locators = Locators()


    @allure.step('Проверка. Количество клиентов = 6')
    def check_new_one_customer_added(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        customer_count = len(customers) // 3
        assert customer_count == 6, "Количество клиентов не равно 6"


    @allure.step('Проверка. Имена отсортированы в обратном алфавитном порядке')
    def check_first_name_reverse_sort(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        names = Sf.chunks_to_names(customers)
        assert names == sorted(names, reverse=True), "Имена не отсортированы в обратном алфавитном порядке"


    @allure.step('Проверка. Имена отсортированы по алфавиту')
    def check_first_name_sort(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        names = Sf.chunks_to_names(customers)
        assert names == sorted(names), "Имена не отсортированы в алфавитном порядке"


    @allure.step('Проверка. Имя "Harry" удалено')
    def check_delete_customer(self):
        customers = self.find_elements(self.locators.CUSTOMERS_MAIN_DATA_LOCATOR)
        names = Sf.chunks_to_names(customers)
        assert 'Harry' not in names, "Имя Harry не удалено"
