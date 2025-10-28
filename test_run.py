from pages.add_customer import AddCustomer
from pages.customers import Customers
from helpers.checks import Checks


def test_1(driver):
    #  Предусловие 1 : Открыть браузер
    add_customer = AddCustomer(driver)
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    add_customer.open()

    #  Ожидание загрузки страницы
    add_customer.wait_for_page_load()

    #  Предусловие 3 : Перейти на нужную форму
    add_customer.click_add_customer()

    #  Ожидание загрузки формы
    add_customer.wait_for_form_load()

    #  Проверяем готовность к выполнению
    checks.add_customer_form_loaded()


    customers.open()
    customers.wait_for_page_load()
    customers.click_customers()
    customers.wait_for_form_load()
    checks.customers_form_loaded()