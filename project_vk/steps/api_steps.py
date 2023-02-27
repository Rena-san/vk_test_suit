from project_vk.project_api_vk.api_vk import ApiVk


class ApiSteps:

    @staticmethod
    def edit_wall_post_adn_add_pic(post_id, new_text):
        upload_url = ApiVk().get_upload_url()
        photo, server, photo_hash = ApiVk().send_pic_to_url(upload_url)
        owner_id, photo_id, url = ApiVk().save_photo_before_post(photo,
                                                                 server,
                                                                 photo_hash)
        post_id, photo_name = ApiVk().edit_wall_post(new_text,
                                                     post_id,
                                                     owner_id,
                                                     photo_id)
        return post_id, url
