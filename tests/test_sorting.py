from seleniumbase import BaseCase
from pages.main_page import MainPage
from pages.results_page import ResultsPage
from src.data_sets import ResultsData
from parameterized import parameterized


class TestSorting(BaseCase):
    def setUp(self):
        super(TestSorting, self).setUp()
        MainPage().open_main_page(self)

    @parameterized.expand(ResultsData.searching_products)
    def test_sorting_by_lowest_price(self, searching_products):
        MainPage().input_search_product(self, searching_products)
        ResultsPage().sort_list(self)
        ResultsPage().prices_string(self)
        ResultsPage().prices_float(self, ResultsPage().prices_string(self))


# add test to check whether click on lowest price xxxx ???
# add parametrized   xxxx
# should print price of search product   xxxx
# remove html from github
# push to new branch
