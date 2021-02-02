from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class NyTimes(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://cooking.nytimes.com"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://cooking.nytimes.com/search?q={query}&page={index}'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        # Simple HTML lookups.
        recipes = soup.find_all('article', class_='recipe-card')
        results : List[RecipeLink] = []
        for recipe in recipes:
            title_block = recipe.find('div', class_='card-info-wrapper').find('a', class_='card-link')
            link = self.parse_link(title_block.get('href'))
            title = title_block.find('h3').string
            results.append(RecipeLink(title.strip(), link, self.host()))
        return results