from ._result import SearchResult, RecipeLink
from typing import Dict, List
import requests
import urllib.parse
from bs4 import BeautifulSoup as BS
import tldextract
from ._logger import Logger

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
}


class AbstractSearcher():

    def __init__(self, timeout = None):
        self.timeout = timeout

    @classmethod
    def host(cls):
        """ returns the host of the searcher """
        raise NotImplementedError("This should be implemented")
    
    def build_url(self, keyword, index):
        """ builds the search url, so we can incrementally search pages """
        raise NotImplementedError("This should be implemented")

    def search(self, keyword, limit_per_searcher = -1) -> SearchResult:
        """ returns search results from the chosen website """
        Logger.info(f'Searching {self.host()} for {keyword}')
        all_recipes : SearchResult = SearchResult(keyword, {})
        found = True
        index = 1
        while(found):
            url = self.build_url(keyword, index)

            # Use tldextract to extra just the domain
            site = tldextract.extract(url)

            # Make a new SearchResult with the result of the method fetch_results as parameter.
            recipes = SearchResult(keyword, {site.domain : self.fetch_results(url, keyword, index)})

            # If we found recipes, merge them with what we previously found.
            if recipes.length > 0:
                all_recipes = all_recipes.merge(recipes)
                if limit_per_searcher > 0 and all_recipes.length >= limit_per_searcher:
                    found = False
                else:
                    found = True

                index = index + 1
            else:
                found = False

        return all_recipes

    def fetch_results(self, url, keyword = "", index = 1) -> List[RecipeLink]:
        """ returns all the search results from the chosen website """
        try:
            # Fetching the page and passing it to Beautiful soup should be the
            # same for every searcher. Otherwise this function can be overridden
            # as well.
            page_data = requests.get(
                url, headers=HEADERS, timeout=self.timeout
            ).content
            soup = BS(page_data, "html.parser")

            # Parsing, which has an own implementation per searcher.
            return self.parse_results(soup)
        except Exception as e:
            Logger.error(f"Could not get any recipes from {url} because {type(e)}")
        return []
        

    def parse_results(self, soup) -> List[RecipeLink]:
        """ parse the results from a soup object """
        raise NotImplementedError("This should be implemented")

    def parse_link(self, link : str) -> str:
        if link.startswith("http") or link.startswith(self.host()):
            return link
        return self.host() + link