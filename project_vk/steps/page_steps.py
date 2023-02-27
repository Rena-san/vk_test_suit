from project_vk.page_object.login_page import LoginPage


class PageSteps:

    @staticmethod
    def authorization(email, password):
        login_page = LoginPage()
        login_page.login_form.is_opened()
        login_page.login_form.type_email(email)
        login_page.login_form.click_sign_btn()
        login_page.password_form.is_opened()
        login_page.password_form.type_password(password)
        login_page.password_form.click_continue_btn()
