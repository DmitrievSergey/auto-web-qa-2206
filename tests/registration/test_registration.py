import pytest

from src.page_objects.RegistrationPage import RegistrationPage


def test_search(browser):
    RegistrationPage(browser) \
        .open_registration_page() \
        .verify_your_personal_details_text_presence() \
        .verify_email_input_presence() \
        .verify_firstname_input_presence() \
        .verify_register_account_text_presence() \
        .verify_lastname_input_presence()


@pytest.mark.parametrize('first_name, last_name, email, telephone, pwd, cpwd',
                         [('first_name3', 'last_name3', 'fl3@mail.com', '32233322', '1234', '1234')])
def test_add_user(browser, first_name, last_name, email, telephone, pwd, cpwd):
    RegistrationPage(browser) \
        .open_registration_page() \
        .fill_firstname(first_name) \
        .fill_lastname(last_name) \
        .fill_email(email) \
        .fill_telephone(telephone) \
        .fill_password(pwd) \
        .fill_confirm(cpwd) \
        .click_privacy_policy() \
        .click_continue()
    assert RegistrationPage(browser).get_success_title() == "Your Account Has Been Created!"
