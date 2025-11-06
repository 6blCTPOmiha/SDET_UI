from selenium.webdriver.common.by import By


class Locators:
    ADD_CUSTOMER_MAIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
    CUSTOMERS_MAIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[type = "submit"]')
    FIRST_NAME_TEXT_BOX_LOCATOR = (By.CSS_SELECTOR, '[ng-model="fName"]')
    LAST_NAME_TEXT_BOX_LOCATOR = (By.CSS_SELECTOR, '[ng-model="lName"]')
    POST_CODE_TEXT_BOX_LOCATOR = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    HERMOINE_LABEL_LOCATOR = (By.XPATH,  '//td[contains(text(), "Hermoine")]')
    FIRST_NAME_HYPERTEXT_LOCATOR = (By.XPATH,  '//a[contains(text(), "First Name")]')
    DELETE_BUTTONS_LOCATOR = (By.CSS_SELECTOR, '[ng-click="deleteCust(cust)"]')
    CUSTOMERS_MAIN_DATA_LOCATOR = (By.CSS_SELECTOR,  '[class="ng-binding"]')
