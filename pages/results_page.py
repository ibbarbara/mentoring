from src.selectors import GeneralSelectors
from src.selectors import ResultsPageSelectors
import logging as logger

# logging.basicConfig(level=logging.INFO)


class ResultsPage:
    def sort_list(self, sb):
        sb.click_chain(
            [ResultsPageSelectors.SORT_DD, ResultsPageSelectors.LOWEST_PRICE_DD]
        )
        sb.click(GeneralSelectors.USER_CT)

    def prices_string(self, sb):
        prices = sb.find_elements(ResultsPageSelectors.PRICES_TXT)
        prices_string_list = []
        for elem in prices:
            if elem.text:
                elem_r = (elem.text[:-3]).replace(",", ".")
                prices_string_list.append(elem_r)
        return prices_string_list

    def prices_float(self, sb, prices_txt_list):
        prices_float_list = list(map(float, prices_txt_list))
        min_price = min(prices_float_list)
        try:
            min_price_txt = (str(min_price).replace(".", ",")) + " zł aktualna cena"
            logger.info(f"The minimum price is {min_price} zł")
            sb.click_xpath(f"//span[@aria-label='{min_price_txt}']")
        except:
            logger.info("The product doesn't belong to category and is not clickable")
