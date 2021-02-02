from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class BonAppetit(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://www.bonappetit.com/"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://www.bonappetit.com/search/{query}?page={index}'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        # Simple HTML lookups.
        recipes = soup.find_all('article', class_='recipe-content-card')
        results : List[RecipeLink] = []
        for recipe in recipes:
            title_block = recipe.find('h4').find('a')
            link = self.parse_link(title_block.get('href'))
            title = title_block.string
            results.append(RecipeLink(title, link, self.host()))
        return results