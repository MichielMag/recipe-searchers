from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
import requests
import json
from typing import List


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7",
    "X-Requested-With": "XMLHttpRequest"
}

class JamieOliver(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://www.jamieoliver.com"
    
    def build_url(self, keyword, index):
        start = (index - 1) + (index - 1) * 12
        query = urllib.parse.quote_plus(keyword)
        return f'https://www.jamieoliver.com/search/query?s={query}&type=recipe&start={start}'
        
    def parse_results(self, obj) -> List[RecipeLink]:
        results : List[RecipeLink] = []

        for result in obj['search']:
            results.append(RecipeLink(result['title'], result['permalink'], self.host()))

        return results
    
    def fetch_results(self, url, keyword = "", index = 1) -> List[RecipeLink]:
        """ returns all the search results from the chosen website """
        try:
            page_data = requests.get(
                url, headers=HEADERS, timeout=self.timeout
            ).content

            #print(page_data)
            
            return self.parse_results(json.loads(page_data))
        except Exception as e:
            pass
        return []