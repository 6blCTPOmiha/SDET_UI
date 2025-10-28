from data.text_data import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Customers:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get(URL)


    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
        ), message='Страница не загружается')


    def click_customers(self):
        customers_button = self.driver.find_element(By.CSS_SELECTOR, '[ng-class="btnClass3"]')
        customers_button.click()


    def wait_for_form_load(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//td[contains(text(), "Hermoine")]')
        ), message='Форма не загружается')
