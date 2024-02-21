import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s
from qality_lab_demoqa.data.users import TextFormUser, Alex
from qality_lab_demoqa.helpers.skip_onboarding import skip_onboarding_question


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
        browser.open('/text-box')
        return self

    @allure.step('Принимаем согласие')
    def accept_the_consent(self):
        skip_onboarding_question()

    @allure.step('Проверка заголовка имени формы')
    def should_title_form(self):
        self.should_title_element.should(have.text('Text Box'))

    @allure.step('Заполнение и отправка формы')
    def filling_out_the_form(self, user: TextFormUser):
        self.full_name_user.should(be.visible).type(user.full_name)
        self.email_user.should(be.visible).type(user.user_email)
        self.current_adress_user.should(be.visible).type(
            f'{user.current_city}, {user.current_street}, {user.current_house}, {user.current_flat}'
        )
        self.permanent_adress_user.should(be.visible).type(
            f'{user.permanent_city}, {user.permanent_street}, {user.permanent_house}, {user.permanent_flat}'
        )
        self.submit_button.press_enter()

    @allure.step('Проверка заполнения полей ответа формы')
    def verify_search_results_title(self, user):
        self.output.should(be.visible).should(
            have.exact_text(
                f'Name:{user.full_name}\n'
                f'Email:{user.user_email}\n'
                f'Current Address :{user.current_city}, {user.current_street}, {user.current_house}, {Alex.current_flat}\n'
                f'Permananet Address :{user.permanent_city}, {user.permanent_street}, {user.permanent_house}, {user.permanent_flat}'
            )
        )
