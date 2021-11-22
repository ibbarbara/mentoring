from seleniumbase import BaseCase
from src.data_sets import LogInData
from parameterized import parameterized
from pages.login_page import LoginPage


class TestLogInPage(BaseCase):
    def setUp(self):
        # dopisujemy to co mamy w TestLogInPage klasie, do klasy BaseCase, jeśli brak super() to nadpiszemy to co w kalsie BaseCase
        super(TestLogInPage, self).setUp()
        LoginPage().open_logging_page(self)

    @parameterized.expand(LogInData.credentials)
    def test_logging_wrong_credentials(self, credentials):
        LoginPage().input_credentials(self, credentials)
        LoginPage().click_log_in(self)
        LoginPage().assert_error_message(self)
