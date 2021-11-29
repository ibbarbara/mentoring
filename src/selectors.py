class GeneralSelectors:
    CONSENT = 'button[data-role="accept-consent"]'
    USER_CT = 'div[data-role="aboveItems"]'


class LogInPageSelectors:
    LOGIN_BTN = 'button[role="button"]'
    EMAIL_IB = 'input[id="login"]'
    PASSWD_IB = 'input[id="password"]'
    ERROR_TB = 'div[id="login-form-submit-error"]'


class MainPageSelectors:
    SEARCH_IB = 'input[data-role="search-input"]'
    SEARCH_BTN = 'button[data-role="search-button"]'


class ResultsPageSelectors:
    SORT_DD = 'select[id="allegro.listing.sort"]'
    LOWEST_PRICE_DD = 'option[value="p"]'
    PRODUCTS_PRICE = '//span[@class="_1svub _lf05o"]'
