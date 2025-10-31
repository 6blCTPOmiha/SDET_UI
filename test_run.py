import allure
from pages.add_customer import AddCustomer
from pages.customers import Customers
from helpers.checks import Checks


@allure.story('Тестирование добавления нового пользователя')
def test_positive_add_customer(driver):
    #  Предусловие 1 : Открыть браузер
    add_customer = AddCustomer(driver)
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    add_customer.open()

    #  Ожидание загрузки страницы
    add_customer.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Add customer"
    add_customer.click_add_customer()

    #  Ожидание загрузки формы
    add_customer.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.add_customer_form_loaded()

    #  Шаг 3 : Вводим имя
    add_customer.input_first_name()

    #  Шаг 4 : Вводим фамилию
    add_customer.input_last_name()

    #  Шаг 5 : Вводим код
    add_customer.input_post_code()

    #  Шаг 6 : Нажимаем на кнопку подтверждения введённых данных
    add_customer.click_add_customer_button()

    #  Шаг 7 : Нажимаем ОК в уведомлении
    add_customer.ok_alert_message()

    #  Шаг 8 : Нажимаем на кнопку "Customers" (переходим к списку пользователей)
    customers.click_customers()
    customers.wait_for_form_load()

    #  Шаг 9 : Проверяем количество пользователей
    checks.new_one_customer_added()



@allure.story('Тестирование сортировки в 2 стороны')
def test_positive_customers_name_sort(driver):
    #  Предусловие 1 : Открыть браузер
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    customers.open()

    #  Ожидание загрузки страницы
    customers.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Customers"
    customers.click_customers()

    #  Ожидание загрузки формы
    customers.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.customers_form_loaded()

    #  Шаг 3 : Кликаем на "First Name"
    customers.click_first_name()

    #  Шаг 4 : Проверяем на обратную сортировку
    checks.first_name_reverse_sort()

    #  Шаг 5 : Снова кликаем на "First Name"
    customers.click_first_name()

    #  Шаг 6 : Проверяем на сортировку
    checks.first_name_sort()


@allure.story('Тестирование удаления пользователя')
def test_positive_customer_delete(driver):
    #  Предусловие 1 : Открыть браузер
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    customers.open()

    #  Ожидание загрузки страницы
    customers.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Customers"
    customers.click_customers()

    #  Ожидание загрузки формы
    customers.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.customers_form_loaded()

    #  Шаг 3 : Удаляем нужного клиента
    customers.delete_close_name()

    #  Шаг 4 : Проверяем, удалился ли нужный клиент
    checks.delete_customer_check()


@allure.story('Тестирование добавления нового пользователя')
def test_negative_add_customer(driver):

    #  Предусловие 1 : Открыть браузер
    add_customer = AddCustomer(driver)
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    add_customer.open()

    #  Ожидание загрузки страницы
    add_customer.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Add customer"
    add_customer.click_add_customer()

    #  Ожидание загрузки формы
    add_customer.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.add_customer_form_loaded()

    #  Шаг 3 : Вводим имя
    add_customer.input_first_name()

    #  Шаг 4 : Вводим фамилию
    add_customer.input_last_name()

    #  Шаг 5 : Вводим код
    add_customer.input_post_code()

    #  Шаг 6 : Нажимаем на кнопку "Customers" (переходим к списку пользователей)
    customers.click_customers()
    customers.wait_for_form_load()

    #  Шаг 7 : Проверяем количество пользователей
    checks.new_one_customer_added()


@allure.story('Тестирование сортировки в 2 стороны')
def test_negative_customers_name_sort(driver):
    #  Предусловие 1 : Открыть браузер
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    customers.open()

    #  Ожидание загрузки страницы
    customers.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Customers"
    customers.click_customers()

    #  Ожидание загрузки формы
    customers.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.customers_form_loaded()

    #  Шаг 3 : Кликаем на "First Name"
    customers.click_first_name()

    #  Шаг 4 : Проверяем на сортировку
    checks.first_name_sort()


@allure.story('Тестирование удаления пользователя')
def test_negative_customer_delete(driver):
    #  Предусловие 1 : Открыть браузер
    customers = Customers(driver)
    checks = Checks(driver)

    #  Предусловие 2 : Перейти по ссылке
    customers.open()

    #  Ожидание загрузки страницы
    customers.wait_for_page_load()

    #  Шаг 1 : Нажимаем на "Customers"
    customers.click_customers()

    #  Ожидание загрузки формы
    customers.wait_for_form_load()

    #  Шаг 2 : Проверяем загрузку формы
    checks.customers_form_loaded()

    #  Шаг 3 : Удаляем клиента, который не подходит под условие
    customers.delete_wrong_name()

    #  Шаг 4 : Проверяем, удалился ли нужный клиент
    checks.delete_customer_check()
