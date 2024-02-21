import allure
from selene.support.shared.jquery_style import s, ss
from selene import be, have


@allure.step('Skip send notifications')
def skip_onboarding_question():
    if (
        ss('.fc-button-label')
        .element_by(have.text('Manage options'))
        .matching(be.clickable)
    ):
        ss('.fc-button-label').element_by(have.text('Consent')).click()
