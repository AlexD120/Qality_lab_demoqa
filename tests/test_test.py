import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s, ss
import time

FULL_NAME = "Alex Davydov"
USER_EMAIL = "Gredtx@gmail.com"
CURRENT_CITY = "Stavropol"
CURRENT_STREET = "South"
CURRENT_HOUSE = "88 b"
CURRENT_FLAT = "12 a"

PERMANENT_CITY = "Moscow"
PERMANENT_STREET = "Bolshaya Sadovaya"
PERMANENT_HOUSE = "302-bis"
PERMANENT_FLAT = "50"


def test_text_box():
    browser.open("https://demoqa.com/text-box")
    s('.text-center').should(have.text('Text Box'))
    s('#userName').type(FULL_NAME)
    s('#userEmail').type(USER_EMAIL)
    s('#currentAddress').type(
        f'{CURRENT_CITY}, {CURRENT_STREET}, {CURRENT_HOUSE}, {CURRENT_FLAT}'
    )
    s('#permanentAddress').type(
        f'{PERMANENT_CITY}, {PERMANENT_STREET}, {PERMANENT_HOUSE}, {PERMANENT_FLAT}'
    )
    s('#submit').press_enter()
    s('#output').should(
        have.exact_text(
            f'Name:{FULL_NAME}\n'
            f'Email:{USER_EMAIL}\n'
            f'Current Address :{CURRENT_CITY}, {CURRENT_STREET}, {CURRENT_HOUSE}, {CURRENT_FLAT}\n'
            f'Permananet Address :{PERMANENT_CITY}, {PERMANENT_STREET}, {PERMANENT_HOUSE}, {PERMANENT_FLAT}'
        )
    )

    time.sleep(5)
