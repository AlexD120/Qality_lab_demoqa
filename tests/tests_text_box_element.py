import allure
from qality_lab_demoqa.helpers.application import app
from qality_lab_demoqa.data.users import Alex


def test_text_box():
    app.simple_form_filling_text_box_element_page.open()
    app.simple_form_filling_text_box_element_page.should_title_form()
    app.simple_form_filling_text_box_element_page.filling_out_the_form(Alex)
    app.simple_form_filling_text_box_element_page.verify_search_results_title(Alex)
