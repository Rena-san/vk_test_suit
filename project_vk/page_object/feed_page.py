from selenium.webdriver.common.by import By

from framework.elements.link import Link
from framework.pages.base_page import BasePage


class FeedPage(BasePage):
    UNIQ_ELEMENT = '//*[@id="feed_wall"]'
    MY_PAGE_LINK = '//*[@id="l_pr"]//*[contains(@class, "left_label")]'

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator=FeedPage.UNIQ_ELEMENT,
                         page_name='FeedPage')

    def click_my_page(self):
        Link(By.XPATH, self.MY_PAGE_LINK, "ссылка на персональную страницу пользователя").click()
