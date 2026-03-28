import allure
import pytest

from pages.add_customer.add_customer_page import AddCustomerPage
from pages.customers.customers_page import CustomersPage
from pages.customers.customers_checks import CustomersChecks


@allure.feature('Тестирование работы с клиентами')
class TestRun:

    @allure.story('Позитивные тесты')
    @allure.title('Добавление клиента')
    @pytest.mark.positive
    @pytest.mark.add_customer
    def test_positive_add_customer(self, driver):
        add_customer_page = AddCustomerPage(driver)
        customers_page = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        add_customer_page.open_page()
        add_customer_page.wait_for_page_load()
        add_customer_page.click_add_customer()
        add_customer_page.wait_for_form_load()
        add_customer_page.input_first_name()
        add_customer_page.input_last_name()
        add_customer_page.input_post_code()
        add_customer_page.click_add_customer_button()
        add_customer_page.click_ok_alert_message()
        customers_page.click_customers()
        customers_page.wait_for_form_load()
        customers_checks.check_new_one_customer_added()


    @allure.story('Позитивные тесты')
    @allure.title('Сортировка клиентов по имени')
    @pytest.mark.positive
    @pytest.mark.name_sort
    def test_positive_customers_name_sort(self, driver):
        customers = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        customers.open_page()
        customers.wait_for_page_load()
        customers.click_customers()
        customers.wait_for_form_load()
        customers.click_first_name()
        customers_checks.check_first_name_reverse_sort()
        customers.click_first_name()
        customers_checks.check_first_name_sort()


    @allure.story('Позитивные тесты')
    @allure.title('Удаление клиента')
    @pytest.mark.positive
    @pytest.mark.delete
    def test_positive_customer_delete(self, driver):
        customers = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        customers.open_page()
        customers.wait_for_page_load()
        customers.click_customers()
        customers.wait_for_form_load()
        customers.delete_close_name()
        customers_checks.check_delete_customer()


    @allure.story('Негативные тесты')
    @allure.title('Добавление клиента')
    @pytest.mark.negative
    @pytest.mark.add_customer
    def test_negative_add_customer(self, driver):
        add_customer = AddCustomerPage(driver)
        customers = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        add_customer.open_page()
        add_customer.wait_for_page_load()
        add_customer.click_add_customer()
        add_customer.wait_for_form_load()
        add_customer.input_first_name()
        add_customer.input_last_name()
        add_customer.input_post_code()
        customers.click_customers()
        customers.wait_for_form_load()
        customers_checks.check_new_one_customer_added()


    @allure.story('Негативные тесты')
    @allure.title('Сортировка клиентов по имени')
    @pytest.mark.negative
    @pytest.mark.name_sort
    def test_negative_customers_name_sort(self, driver):
        customers = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        customers.open_page()
        customers.wait_for_page_load()
        customers.click_customers()
        customers.wait_for_form_load()
        customers.click_first_name()
        customers_checks.check_first_name_sort()


    @allure.story('Негативные тесты')
    @allure.title('Удаление клиента')
    @pytest.mark.negative
    @pytest.mark.delete
    def test_negative_customer_delete(self, driver):
        customers = CustomersPage(driver)
        customers_checks = CustomersChecks(driver)
        customers.open_page()
        customers.wait_for_page_load()
        customers.click_customers()
        customers.wait_for_form_load()
        customers.delete_wrong_name()
        customers_checks.check_delete_customer()
