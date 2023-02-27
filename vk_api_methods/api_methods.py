import requests

from vk_api_methods.constans.api_vk_methods import ApiVKMethods


class VkApiMethods:

    def __init__(self, api_url, token,
                 api_version, user_id=None, domain=None):
        self.api_url = api_url
        self.token = token
        self.api_version = api_version
        self.user_id = user_id
        self.domain = domain

    def post_on_wall(self, text, owner_id=None, pic_id=None):
        resp_post = requests.post(self.api_url + ApiVKMethods.POST_ON_WALL,
                                  params={
                                      "access_token": self.token,
                                      "v": self.api_version,
                                      "domain": self.domain,
                                      "message": text,
                                      "attachments": f'photo{owner_id}_{pic_id}'
                                     }
                                  ).json()
        return resp_post["response"]["post_id"]

    def edit_wall_post(self, new_text, post_id, owner_id=None, pic_id=None):
        resp_post = requests.post(self.api_url + ApiVKMethods.EDIT_WALL_POST,
                                  params={
                                      "access_token": self.token,
                                      "v": self.api_version,
                                      "post_id": post_id,
                                      "domain": self.domain,
                                      "message": new_text,
                                      "attachments": f'photo{owner_id}_{pic_id}'
                                    }
                                  ).json()
        return resp_post["response"]["post_id"]

    def get_upload_url(self):
        resp_url = requests.post(self.api_url + ApiVKMethods.PIC_UPLOAD_ON_SERVER,
                                 params={
                                     "access_token": self.token,
                                     "v": self.api_version,
                                 }
                                 ).json()
        return resp_url["response"]["upload_url"]

    @staticmethod
    def send_pic_to_url(upload_url, image_path):
        file = {"file1": open(f"{image_path}", "rb")}
        response_photo = requests.post(upload_url, files=file).json()
        return (response_photo["photo"],
                response_photo["server"],
                response_photo["hash"])

    def save_photo_before_post(self, photo, server, photo_hash):
        save_photo = requests.post(self.api_url + ApiVKMethods.PIC_SAVE_BEFORE_POST,
                                   params={
                                       "access_token": self.token,
                                       "v": self.api_version,
                                       "user_id": self.user_id,
                                       "photo": photo,
                                       "server": server,
                                       "hash": photo_hash
                                     }
                                   ).json()
        return (save_photo["response"][0]["owner_id"],
                save_photo["response"][0]["id"],
                save_photo["response"][0]["sizes"][5]["url"])

    def create_post_comment(self, text, post_id):
        resp_comment = requests.post(self.api_url + ApiVKMethods.CREAT_COMMENT,
                                     params={
                                         "access_token": self.token,
                                         "v": self.api_version,
                                         "owner_id": self.user_id,
                                         "post_id": post_id,
                                         "message": text
                                     }
                                     ).json()
        return resp_comment["response"]["comment_id"]

    def get_post_likes(self, post_id):
        resp_comment = requests.get(self.api_url + ApiVKMethods.GET_POST_LIKES,
                                    params={
                                        "access_token": self.token,
                                        "v": self.api_version,
                                        "owner_id": self.user_id,
                                        "post_id": post_id,
                                      }
                                    ).json()

        return resp_comment["response"]["count"]

    def delete_post(self, post_id):
        resp = requests.post(self.api_url + ApiVKMethods.DELETE_POST,
                             params={
                                 "access_token": self.token,
                                 "v": self.api_version,
                                 "owner_id": self.user_id,
                                 "post_id": post_id,
                               }
                             ).json()
        return resp["response"]
