import allure
from qality_lab_demoqa.helpers.application import app
from qality_lab_demoqa.data.users import Alex


@allure.title("Проверка корректного заполнения формы текстового поля")
@allure.feature("Простая форма")
@allure.story("Заполнение информации о пользователе")
@allure.label("UI")
@allure.tag("smoke")
@allure.severity("normal")
@allure.label("owner", "Davydov")
def test_text_box(browser_config):
    # ARRANGE
    app.simple_form_filling_text_box_element_page.open()
    app.simple_form_filling_text_box_element_page.accept_the_consent()
    app.simple_form_filling_text_box_element_page.should_title_form()

    # ACT
    app.simple_form_filling_text_box_element_page.filling_out_the_form(Alex)

    # ASSERT
    app.simple_form_filling_text_box_element_page.verify_search_results_title(Alex)
