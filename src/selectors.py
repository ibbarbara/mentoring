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
    OFFERT_TXT = (
        'h2[class="mgmw_wo mgn2_21 mp0t_ji m9qz_yo mqu1_1j mp4t_8 mryx_8 m7er_k4"]'
    )
    PRICES_TXT = 'span[class="_1svub _lf05o"]'
