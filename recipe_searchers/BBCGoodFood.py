from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class BBCGoodFood(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://www.bbcgoodfood.com"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://www.bbcgoodfood.com/search/recipes/page/{index}/?q={query}&sort=-relevance'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        recipes = soup.find_all('div', class_='standard-card-new')
        results : List[RecipeLink] = []
        for recipe in recipes:
            title_block = recipe.find('a', class_='standard-card-new__article-title')
            link = self.parse_link(title_block.get('href'))
            title = title_block.string
            results.append(RecipeLink(title, link, self.host()))
        return results