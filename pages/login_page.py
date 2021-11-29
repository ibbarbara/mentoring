# from logging import error
# from cssselect.parser import Selector
from src.constants import Constants
from src.selectors import LogInPageSelectors
from src.selectors import GeneralSelectors
from src.data_sets import LogInData
import assertpy


class LoginPage:
    def open_logging_page(self, sb):
        sb.open(Constants.url + "logowanie")
        sb.click(GeneralSelectors.CONSENT)
        sb.find_element(LogInPageSelectors.LOGIN_BTN)

    ####dlaczego taki zapisa credentials[LoginData.EMAIL]
    def input_credentials(self, sb, credentials: dict):
        sb.type(LogInPageSelectors.EMAIL_IB, credentials[LogInData.EMAIL])
        sb.type(LogInPageSelectors.PASSWD_IB, credentials[LogInData.PASSWORD])

    def click_log_in(self, sb):
        sb.click(LogInPageSelectors.LOGIN_BTN)

    def assert_error_message(self, sb):
        error_text = sb.get_text(LogInPageSelectors.ERROR_TB)
        assertpy.assert_that(error_text).contains(
            "Login, e-mail lub hasło są nieprawidłowe"
        )

    # wrzucic na repo
    # .gitignore
    # konfiguracja ściezki do trzymania raportów
