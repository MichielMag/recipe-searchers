from ._abstract import AbstractSearcher
from ._result import RecipeLink, SearchResult
import urllib.parse
from typing import List

class HostTheToast(AbstractSearcher):
    def __init__(self):
        AbstractSearcher.__init__(self)

    @classmethod
    def host(cls):
        return "https://hostthetoast.com"
    
    def build_url(self, keyword, index):
        query = urllib.parse.quote_plus(keyword)
        return f'https://hostthetoast.com/page/{index}/?s={query}&searchsubmit=GO'
        
    def parse_results(self, soup) -> List[RecipeLink]:
        recipes = soup.find_all('article', class_='post')
        results : List[RecipeLink] = []
        for recipe in recipes:
            title_block = recipe.find('a', class_='entry-title-link')
            link = self.parse_link(title_block.get('href'))
            title = title_block.string
            results.append(RecipeLink(title, link, self.host()))
        return results