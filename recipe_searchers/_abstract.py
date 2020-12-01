from ._exception_handling import ExceptionHandlingMetaclass
from ._result import SearchResult, RecipeLink
from typing import Dict, List
import requests
import urllib.parse
from bs4 import BeautifulSoup as BS

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
}


class AbstractSearcher(metaclass=ExceptionHandlingMetaclass):

    def __init__(self, timeout = None):
        self.timeout = timeout

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
            recipes = SearchResult(keyword, {self.host() : self.fetch_results(url, keyword, index)})
            if recipes.length > 0:
                all_recipes = all_recipes.merge(recipes)
                found = True
                index = index + 1
            else:
                found = False
        return all_recipes

    def fetch_results(self, url, keyword = "", index = 1) -> List[RecipeLink]:
        """ returns all the search results from the chosen website """
        try:
            page_data = requests.get(
                url, headers=HEADERS, timeout=self.timeout
            ).content
            soup = BS(page_data, "html.parser")
            return self.parse_results(soup)
        except Exception as e:
            print(f"Could not get any recipes from {url} because {type(e)}")
        return []
        

    def parse_results(self, soup) -> List[RecipeLink]:
        """ parse the results from a soup object """
        raise NotImplementedError("This should be implemented")

    def parse_link(self, link : str) -> str:
        if link.startswith("http") or link.startswith(self.host()):
            return link
        return self.host() + link