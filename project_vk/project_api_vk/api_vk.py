from framework.utils.string_util import set_random_string
from vk_api_methods.constans.api_url import ApiUrl
from vk_api_methods.constans.api_versions import ApiVersion
from project_vk.test_data.access_data import AccessData
from project_vk.test_data.path_to_pic import PATH_TO_PIC
from vk_api_methods.api_methods import VkApiMethods


class ApiVk:
    RANDOM_TEXT = set_random_string()
    TOKEN = AccessData.ACS_TOKEN
    API_URL = ApiUrl.API_URL
    API_VERS = ApiVersion.API_VERSION
    DOMAIN = AccessData.DOMAIN
    USER_ID = AccessData.USER_ID

    def post_on_wall(self, text, owner_id=None, photo_id=None):
        post_id = VkApiMethods(self.API_URL,
                               self.TOKEN,
                               self.API_VERS,
                               self.DOMAIN).post_on_wall(text, owner_id, photo_id)
        return post_id

    def edit_wall_post(self, new_text, post_id, owner_id=None, photo_id=None):
        post_id = VkApiMethods(self.API_URL,
                               self.TOKEN,
                               self.API_VERS,
                               self.DOMAIN).edit_wall_post(new_text, post_id, owner_id, photo_id)
        return post_id, f'photo{owner_id}_{photo_id}'

    def get_upload_url(self):
        upload_url = VkApiMethods(self.API_URL,
                                  self.TOKEN,
                                  self.API_VERS).get_upload_url()
        return upload_url

    def send_pic_to_url(self, upload_url):
        photo, server, photo_hash = VkApiMethods(self.API_URL,
                                                 self.TOKEN,
                                                 self.API_VERS,

                                                 ).send_pic_to_url(upload_url, PATH_TO_PIC)
        return photo, server, photo_hash

    def save_photo_before_post(self, photo, server, photo_hash):
        owner_id, photo_id, url= VkApiMethods(self.API_URL,
                                          self.TOKEN,
                                          self.API_VERS).save_photo_before_post(photo, server, photo_hash)
        return owner_id, photo_id, url

    def create_post_comment(self, text, post_id):
        comment_id = VkApiMethods(self.API_URL,
                                  self.TOKEN,
                                  self.API_VERS,
                                  self.USER_ID
                                  ).create_post_comment(text, post_id)
        return comment_id

    def get_post_likes(self, post_id):
        count_likes = VkApiMethods(self.API_URL,
                                   self.TOKEN,
                                   self.API_VERS,
                                   self.USER_ID
                                   ).get_post_likes(post_id)
        return count_likes

    def delete_post(self, post_id):
        resp = VkApiMethods(self.API_URL,
                            self.TOKEN,
                            self.API_VERS,
                            self.USER_ID
                            ).delete_post(post_id)
        return resp
