import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s
from qality_lab_demoqa.data.users import TextFormUser, Alex


class SimpleShouldFormFields:
    def __init__(self):
        self.should_title_element = s('.text-center')
        self.full_name_user = s('#userName')
        self.email_user = s('#userEmail')
        self.current_adress_user = s('#currentAddress')
        self.permanent_adress_user = s('#permanentAddress')
        self.submit_button = s('#submit')
        self.output = s('#output')

    @allure.step('Открываем страницу')
    def open(self):
        browser.open('https://demoqa.com/text-box')
        return self

    @allure.step('Проверка заголовка имени формы')
    def should_title_form(self):
        self.should_title_element.should(have.text('Text Box'))

    @allure.step('Заполнение и отправка формы')
    def filling_out_the_form(self, user):
        self.full_name_user.type(user.full_name)
        self.email_user.type(user.user_email)
        self.current_adress_user.type(
            f'{user.current_city}, {user.current_street}, {user.current_house}, {user.current_flat}'
        )
        self.permanent_adress_user.type(
            f'{user.permanent_city}, {user.permanent_street}, {user.permanent_house}, {user.permanent_flat}'
        )
        self.submit_button.press_enter()

    @allure.step('Проверка заполнения полей ответа формы')
    def verify_search_results_title(self, user):
        self.output.should(
            have.exact_text(
                f'Name:{user.full_name}\n'
                f'Email:{user.user_email}\n'
                f'Current Address :{user.current_city}, {user.current_street}, {user.current_house}, {Alex.current_flat}\n'
                f'Permananet Address :{user.permanent_city}, {user.permanent_street}, {user.permanent_house}, {user.permanent_flat}'
            )
        )
