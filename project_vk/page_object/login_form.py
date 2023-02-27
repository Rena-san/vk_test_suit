from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class LoginForm(BasePage):
    UNIQ_ELEMENT = '//*[contains(@class, "VkIdForm__header")]'
    EMAIL_INPUT = '//*[contains(@class, "VkIdForm__input")]'
    SIGN_BTN = '//*[contains(@class, "VkIdForm__signInButton")]'

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator=LoginForm.UNIQ_ELEMENT,
                         page_name='LoginForm')

    def type_email(self, email):
        TextBox(By.XPATH,
                self.EMAIL_INPUT,
                'Поле ввода электронной почты').send_keys_to_element(email)

    def click_sign_btn(self):
        Button(By.XPATH, self.SIGN_BTN, 'Кнопка <Sing in>').click()
