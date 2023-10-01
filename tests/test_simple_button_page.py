from pages.simple_button import SimpleButtonPage
import allure


@allure.feature('Simple_button')
@allure.story('existence')
def test_button_1_exist(browser):
    with allure.step('Open simple button page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Check the button'):
        assert simple_page.button_is_displayed()

@allure.feature('Simple_button')
@allure.story('click_ability')
def test_button_1_clicked(browser):
    with allure.step('Open simple button page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Check the button'):
        simple_page.click_button()
    with allure.step('Check the result'):
        assert 'Failed' == simple_page.result_text