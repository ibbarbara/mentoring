from seleniumbase import BaseCase
from pages.main_page import MainPage
from pages.results_page import ResultsPage
from time import sleep


class TestSorting(BaseCase):
    def setUp(self):
        super(TestSorting, self).setUp()
        MainPage().open_main_page(self)

    def test_sorting_by_lowest_price(self):
        MainPage().input_search_product(self, "choinka bożonarodzeniowa")
        ResultsPage().sort_list(self)

        ResultsPage().lowest_price(self)
        print(ResultsPage().lowest_price(self))
        sleep(5)


# add test to check whether click on lowest price
# add parametrized
# should print price of search product
# remove html from github
# push to new branch
