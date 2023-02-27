import pytest

from framework.utils.logger import Logger
from framework.utils.string_util import set_random_string
from project_vk.project_api_vk.api_vk import ApiVk
from project_vk.page_object.feed_page import FeedPage
from project_vk.page_object.my_page import MyPage
from project_vk.steps.api_steps import ApiSteps
from project_vk.steps.page_steps import PageSteps
from project_vk.test_data.access_data import AccessData
from project_vk.test_data.path_to_pic import PATH_TO_PIC
from project_vk.utils.image_utils import ImageUtils

EMAIL = AccessData.EMAIL
PASS = AccessData.PASS
RANDOM_TEXT = set_random_string()
NEW_RANDOM_TEXT = set_random_string()


@pytest.mark.usefixtures("set_up")
class TestSuit:
    def test_vk(self):
        Logger.info("Шаг 1-2. [UI] Перейти на сайт https://vk.com/. \
                        Авторизоваться.")
        PageSteps.authorization(EMAIL, PASS)

        Logger.info("Шаг 3. [UI] Перейти на Мою страницу")
        feed_page = FeedPage()
        assert feed_page.is_opened(), "Данная страница не feed page"
        feed_page.click_my_page()
        my_page = MyPage()
        assert my_page.is_opened(), "Данная страница не feed page"

        Logger.info("Шаг 4. [API] С помощью запроса к API создать запись со случайно \
                    сгенерированным текстом на стене и получить \
                    id записи из ответа.")
        post_id = ApiVk().post_on_wall(RANDOM_TEXT)
        assert post_id, "post id не получен"

        Logger.info(
            "Шаг 5. [UI] Не обновляя страницу убедиться, что на стене появилась \
            запись с нужным текстом от правильного пользователя."
        )
        assert my_page.get_post_or_comment_text(post_id) == RANDOM_TEXT, (
            "Текст не соответствует"
        )
        page_owner = my_page.get_name_page_owner()
        post_author = my_page.get_name_post_author(post_id)
        assert page_owner == post_author, "Пост оставлен не хозяином страницы"

        Logger.info("Шаг 6. [API] Отредактировать запись через запрос к API - \
                        изменить текст и добавить (загрузить) любую картинку.")
        post_id, url = ApiSteps.edit_wall_post_adn_add_pic(post_id,
                                                           NEW_RANDOM_TEXT)

        Logger.info("Шаг 7. [UI] Не обновляя страницу убедиться, \
                    что изменился текст сообщения и добавилась загруженная \
                    картинка(убедиться, что картинки одинаковые)")
        assert my_page.get_post_or_comment_text(post_id) == NEW_RANDOM_TEXT, (
            'Текст не соответствует'
        )
        assert ImageUtils.difference_images_from_file_url(PATH_TO_PIC, url), (
            'Изображения не совпадают'
        )

        Logger.info("Шаг 8. [API] Используя запрос к API добавить комментарий \
                        к записи со случайным текстом.")
        comment_id = ApiVk().create_post_comment(RANDOM_TEXT, post_id)
        my_page.click_link_to_show_comment(post_id)
        assert my_page.get_post_or_comment_text(comment_id) == RANDOM_TEXT, (
            'Текст не соответствует отправленному'
        )

        Logger.info("Шаг 9. [UI] Не обновляя страницу убедиться, что к нужной \
                    записи добавился комментарий от правильного пользователя")
        comment_author = my_page.get_name_comment_author(comment_id)
        assert page_owner == comment_author, (
            'Коммент оставлен не хозяином страницы'
        )

        Logger.info("Шаг 10. [UI] Через UI оставить лайк к записи.")
        my_page.add_like_to_post(post_id)

        Logger.info("Шаг 11. [API] Через запрос к API убедиться, \
                    что у записи появился лайк от правильного пользователя")
        my_page.wait_like_for_api(post_id)
        count_likes = ApiVk().get_post_likes(post_id)
        assert count_likes, "Лайк не добавлен"

        Logger.info("Шаг 12.[API] Через запрос к API удалить созданную запись")
        resp = ApiVk().delete_post(post_id)
        assert resp, "Пост не удален через апи"

        Logger.info("Шаг 13. [UI] Не обновляя страницу убедиться, \
                        что запись удалена")
        assert not my_page.is_post_deleted(post_id), 'Пост не удален через апи'
