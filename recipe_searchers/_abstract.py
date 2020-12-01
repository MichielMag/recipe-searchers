from ._exception_handling import ExceptionHandlingMetaclass
from ._result import SearchResult, RecipeLink
from typing import Dict, List
from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup as BS

class AbstractSearcher(metaclass=ExceptionHandlingMetaclass):

    def __init__(self, **options):
        self.options = options

    @classmethod
    def host(cls):
        """ returns the host of the searcher """
        raise NotImplementedError("This should be implemented")
    
    def build_url(self, keyword, index):
        """ builds the search url, so we can incrementally search pages """
        raise NotImplementedError("This should be implemented")

    def search(self, keyword) -> SearchResult:
        """ returns search results from the chosen website """
        all_recipes : SearchResult = SearchResult(keyword, {})
        found = True
        index = 1
        while(found):
            url = self.build_url(keyword, index)
            recipes = SearchResult(keyword, {self.host() : self.fetch_results(url)})
            if recipes.length > 0:
                all_recipes = all_recipes.merge(recipes)
                found = True
                index = index + 1
            else:
                found = False
        return all_recipes

    def fetch_results(self, url) -> List[RecipeLink]:
        """ returns all the search results from the chosen website """
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BS(html)
        return self.parse_results(soup)

    def parse_results(self, soup) -> List[RecipeLink]:
        """ parse the results from a soup object """
        raise NotImplementedError("This should be implemented")