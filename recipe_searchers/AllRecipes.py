from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class AllRecipes(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "allrecipes.com"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://www.allrecipes.com/search/results/?wt={query}&page={index}'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        recipes = soup.find_all('article', class_='fixed-recipe-card')
        results : List[RecipeLink] = []
        for recipe in recipes:
            link = recipe.find('a', class_='fixed-recipe-card__title-link').get('href')
            title = recipe.find('span', class_='fixed-recipe-card__title-link').string
            results.append(RecipeLink(title, link, self.host()))
        return results