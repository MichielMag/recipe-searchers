from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class BBCCoUk(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://www.bbc.co.uk"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://www.bbc.co.uk/food/search?q={query}&page={index}'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        recipes = soup.find_all('a', class_='promo')
        results : List[RecipeLink] = []
        for recipe in recipes:
            link = self.parse_link(recipe.get('href'))
            title = recipe.find('h3', class_='promo__title').string
            results.append(RecipeLink(title, link, self.host()))
        return results