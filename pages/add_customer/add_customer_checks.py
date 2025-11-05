import allure
from helpers.base_page import BasePage
from helpers.help_func import StaticFunctions as Sf
from data.locators import Locators


class AddCustomerChecks(BasePage):
    def __init__(self, driver):

        super().__init__(driver)

        self.locators = Locators()
