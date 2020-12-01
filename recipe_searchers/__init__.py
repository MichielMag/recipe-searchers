from .AllRecipes import AllRecipes
from .BBCCoUk import BBCCoUk
from .BBCGoodFood import BBCGoodFood
from .BonAppetit import BonAppetit
from .TheWoksOfLife import TheWoksOfLife
from .Food import Food
from ._result import SearchResult
from typing import List

SEARCHERS = [
    AllRecipes,
    BBCCoUk,
    BBCGoodFood,
    BonAppetit,
    TheWoksOfLife,
    Food
]

def search_recipe(keyword : str) -> SearchResult:
    results : SearchResult = SearchResult(keyword)
    for searcher in SEARCHERS:
        result = searcher().search(keyword)
        results = results.merge(result)

    return results

__all__ = ["search_recipe"]
name = "recipe_searchers"