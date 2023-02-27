from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from project_vk.page_object.login_form import LoginForm
from project_vk.page_object.password_form import PasswordForm


class LoginPage(BasePage):
    UNIQ_ELEMENT = '//*[contains(@class, "VkIdForm__header")]'

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator=LoginPage.UNIQ_ELEMENT,
                         page_name='LoginPage')

    @property
    def login_form(self):
        return LoginForm()

    @property
    def password_form(self):
        return PasswordForm()
