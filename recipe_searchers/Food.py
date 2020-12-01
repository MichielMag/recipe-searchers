from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
import requests
import json
from typing import List

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
    "Content-Type": "application/json"
}

class Food(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://www.food.com/"
    
    def build_url(self, keyword, index):
        return f'https://api.food.com/external/v1/nlp/search'
        
    def parse_results(self, obj) -> List[RecipeLink]:
        results : List[RecipeLink] = []

        for result in obj['response']['results']:
            if result['record_type'] == 'Recipe':
                results.append(RecipeLink(result['main_title'], result['record_url'], self.host()))

        return results
    
    def fetch_results(self, url, keyword = "", index = 1) -> List[RecipeLink]:
        """ returns all the search results from the chosen website """
        try:
            data = {}
            data['contexts'] = []
            data['searchTerm'] = keyword
            data['pn'] = index

            page_data = requests.post(
                url, json=data, headers=HEADERS, timeout=self.timeout
            ).content
            
            return self.parse_results(json.loads(page_data))
        except Exception as e:
            print(f"Could not get any recipes from {url} because {type(e)}")
        return []