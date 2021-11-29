from src.selectors import MainPageSelectors
from src.constants import Constants
from src.selectors import GeneralSelectors


class MainPage:
    def open_main_page(self, sb):
        sb.open(Constants.url)
        sb.click(GeneralSelectors.CONSENT)
        sb.find_element(MainPageSelectors.SEARCH_IB)

    def input_search_product(self, sb, product: str):
        sb.type(MainPageSelectors.SEARCH_IB, product)
        sb.click(MainPageSelectors.SEARCH_BTN)
