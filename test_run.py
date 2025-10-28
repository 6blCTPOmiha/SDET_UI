import allure
from pages.add_customer import AddCustomer
from pages.customers import Customers
from helpers.checks import Checks


@allure.epic('Epic is here')
@allure.feature('Feature is here')
@allure.story('Story is here')
def test_positive_1(driver):
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

    #  Шаг 1 : Вводим имя
    add_customer.input_first_name()

    #  Шаг 2 : Вводим фамилию
    add_customer.input_last_name()

    #  Шаг 3 : Вводим код
    add_customer.input_post_code()

    #  Шаг 4 : Нажимаем на кнопку подтверждения введённых данных
    add_customer.click_add_customer_button()

    #  Шаг 5 : Нажимаем ОК в уведомлении
    add_customer.ok_alert_message()

    #  Шаг 6 : Нажимаем на кнопку "Customers" (переходим к списку пользователей)
    customers.click_customers()
    customers.wait_for_form_load()

    #  Шаг 7 : Проверяем количество пользователей
    checks.new_one_customer_added()


    #  customers.open()
    #  customers.wait_for_page_load()
    #  customers.click_customers()
    #  customers.wait_for_form_load()
    #  checks.customers_form_loaded()


@allure.epic('NO Epic is here')
@allure.feature('NO Feature is here')
@allure.story('NO Story is here')
def test_negative_1(driver):
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

    #  Шаг 1 : Вводим имя
    add_customer.input_first_name()

    #  Шаг 2 : Вводим фамилию
    add_customer.input_last_name()

    #  Шаг 3 : Вводим код
    add_customer.input_post_code()

    #  Шаг 4 : НЕ Нажимаем на кнопку подтверждения введённых данных
    # add_customer.click_add_customer_button()

    #  Шаг 5 : НЕ Нажимаем ОК в уведомлении
    # add_customer.ok_alert_message()

    #  Шаг 6 : Нажимаем на кнопку "Customers" (переходим к списку пользователей)
    customers.click_customers()
    customers.wait_for_form_load()

    #  Шаг 7 : Проверяем количество пользователей
    checks.new_one_customer_added()
