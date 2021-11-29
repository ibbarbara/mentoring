from src.selectors import GeneralSelectors
from src.selectors import ResultsPageSelectors
from selenium.webdriver.common.by import By
import assertpy


class ResultsPage:
    def sort_list(self, sb):
        sb.click_chain(
            [ResultsPageSelectors.SORT_DD, ResultsPageSelectors.LOWEST_PRICE_DD]
        )
        sb.click(GeneralSelectors.USER_CT)

    def lowest_price(self, sb):
        price = sb.find_elements(ResultsPageSelectors.PRODUCTS_PRICE, By.XPATH)
        print(price.text)
        for elem in price:
            print(sb.get_text(elem, By.XPATH))
        assert (price) == "38.99"

        assertpy.assert_that(elem.text).contains("38,99 zł")


result = ResultsPage
print(result.lowest_price())


# create list of all prizes from site and check the one with the lowest price
