from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find_element(self, locator, timeout=10):
        return self.wait_for_specific_element(locator, timeout)


    def find_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))


    @staticmethod
    def click_element(element):
        element.click()


    def click_element_by_locator(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()


    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)


    def is_element_visible(self, locator, timeout=10):
        """Проверить видимость элемента"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def wait_for_specific_element(self, locator, timeout=10):
        """
        Ожидание конкретного элемента на странице
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент '{locator[1]}' не найден за {timeout} секунд")


    def is_presence_of_element_located(self, locator, timeout=10):
        """Проверить видимость элемента"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    def wait_for_element_visible(self, locator, timeout=10):
        """Ожидать видимость элемента"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))


    def wait_for_element_clickable(self, locator, timeout=10):
        """Ожидать кликабельность элемента"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))


    def open(self, url):
        self.driver.get(url)


    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.switch_to.default_content()
