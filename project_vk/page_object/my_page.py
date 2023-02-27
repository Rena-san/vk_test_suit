from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.form import Form
from framework.elements.link import Link
from framework.elements.text import Text
from framework.pages.base_page import BasePage
from project_vk.test_data.access_data import AccessData


class MyPage(BasePage):
    UNIQ_ELEMENT = '//*[@id="owner_page_name"]'
    POST = f'//*[@id="post{AccessData.USER_ID}_{id}"]'
    TEXT_POST_COMMENT = f'//*[@id="wpt{AccessData.USER_ID}_{id}"]'
    PAGE_OWNER = '//*[@id="owner_page_name"]'
    POST_AUTHOR = f'//*[@id="post{AccessData.USER_ID}_{id}"]//*[contains(@class, "post_author")]'
    COMMENT_AUTHOR = f'//*[@id="post{AccessData.USER_ID}_{id}"]//*[contains(@class, "reply_author")]'
    LIKE_POST = f'//*[contains(@data-reaction-target-object, "wall{AccessData.USER_ID}_{id}")]'
    DEL_POST = f'//*[@id="post_del{AccessData.USER_ID}_{id}"]'
    SHOW_COMMENT_LINK = f'//*[@id="start_reply{AccessData.USER_ID}_{id}"]//following-sibling::a'
    UPLOADED_IMAGE = f'//*[@id="wpt{AccessData.USER_ID}_{id}"]/div/a'

    def __init__(self):
        super().__init__(search_condition=By.XPATH,
                         locator=MyPage.UNIQ_ELEMENT,
                         page_name='MyPage')

    def get_name_page_owner(self):
        return Text(By.XPATH, self.PAGE_OWNER,
                    'Имя владельца страницы').get_text()

    def get_name_post_author(self, post_id):
        return Text(By.XPATH, self.POST_AUTHOR.format(id=post_id),
                    'Имя автора поста').get_text()

    def get_post_or_comment_text(self, post_id):
        # Ожидание появления элемента установлено для firefox.
        Text(By.XPATH,
             self.TEXT_POST_COMMENT.format(id=post_id),
             'Текст поста/комментария').wait_for_is_displayed(2)
        return Text(By.XPATH,
                    self.TEXT_POST_COMMENT.format(id=post_id),
                    'Текст поста/комментария').get_text()

    def click_link_to_show_comment(self, comment_id):
        Link(By.XPATH, self.SHOW_COMMENT_LINK.format(id=comment_id),
             'Show next comment link').click()

    def get_name_comment_author(self, comment_id):
        return Text(By.XPATH,
                    self.COMMENT_AUTHOR.format(id=comment_id),
                    'Имя автора коммента').get_text()

    def add_like_to_post(self, post_id):
        Button(By.XPATH,
               self.LIKE_POST.format(id=post_id),
               'Кнопка Like').click()

    def wait_like_for_api(self, post_id):
        Button(By.XPATH,
               self.LIKE_POST.format(id=post_id),
               'Кнопка Like').find_element()

    def is_post_deleted(self, post_id):
        try:
            return Form(By.XPATH,
                        self.DEL_POST.format(id=post_id),
                        f"Пост {post_id}").is_exist()
        except ValueError:
            return False
