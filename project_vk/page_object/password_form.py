from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class PasswordForm(BasePage):
    UNIQ_ELEMENT = '//*[contains(@class, "vkc__Password__Wrapper")]'
    PASSWORD_INPUT = '//*[contains(@name, "password")]'
    CONTINUE_BTN = '//*[contains(@type, "submit")]'

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator=PasswordForm.UNIQ_ELEMENT,
                         page_name='PasswordForm')

    def type_password(self, password):
        TextBox(By.XPATH,
                self.PASSWORD_INPUT,
                'Поле ввода электронной почты').send_keys_to_element(password)

    def click_continue_btn(self):
        Button(By.XPATH, self.CONTINUE_BTN, 'Кнопка <Continue>').click()
