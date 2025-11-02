import allure
import pytest

from pages.add_customer import AddCustomer
from pages.customers import Customers
from helpers.checks import Checks


@allure.story('Тестирование добавления нового пользователя')
@pytest.mark.add_customer
def test_positive_add_customer(driver):

    add_customer = AddCustomer(driver)
    customers = Customers(driver)
    checks = Checks(driver)
    add_customer.open()
    add_customer.wait_for_page_load()
    add_customer.click_add_customer()
    add_customer.wait_for_form_load()
    checks.add_customer_form_loaded()
    add_customer.input_first_name()
    add_customer.input_last_name()
    add_customer.input_post_code()
    add_customer.click_add_customer_button()
    add_customer.ok_alert_message()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.new_one_customer_added()



@allure.story('Тестирование сортировки в 2 стороны')
@pytest.mark.name_sort
def test_positive_customers_name_sort(driver):

    customers = Customers(driver)
    checks = Checks(driver)
    customers.open()
    customers.wait_for_page_load()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.customers_form_loaded()
    customers.click_first_name()
    checks.first_name_reverse_sort()
    customers.click_first_name()
    checks.first_name_sort()


@allure.story('Тестирование удаления пользователя')
@pytest.mark.delete
def test_positive_customer_delete(driver):

    customers = Customers(driver)
    checks = Checks(driver)
    customers.open()
    customers.wait_for_page_load()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.customers_form_loaded()
    customers.delete_close_name()
    checks.delete_customer_check()


@allure.story('Тестирование добавления нового пользователя')
@pytest.mark.add_customer
def test_negative_add_customer(driver):

    add_customer = AddCustomer(driver)
    customers = Customers(driver)
    checks = Checks(driver)
    add_customer.open()
    add_customer.wait_for_page_load()
    add_customer.click_add_customer()
    add_customer.wait_for_form_load()
    checks.add_customer_form_loaded()
    add_customer.input_first_name()
    add_customer.input_last_name()
    add_customer.input_post_code()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.new_one_customer_added()


@allure.story('Тестирование сортировки в 2 стороны')
@pytest.mark.name_sort
def test_negative_customers_name_sort(driver):

    customers = Customers(driver)
    checks = Checks(driver)
    customers.open()
    customers.wait_for_page_load()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.customers_form_loaded()
    customers.click_first_name()
    checks.first_name_sort()


@allure.story('Тестирование удаления пользователя')
@pytest.mark.delete
def test_negative_customer_delete(driver):

    customers = Customers(driver)
    checks = Checks(driver)
    customers.open()
    customers.wait_for_page_load()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.customers_form_loaded()
    customers.delete_wrong_name()
    checks.delete_customer_check()
