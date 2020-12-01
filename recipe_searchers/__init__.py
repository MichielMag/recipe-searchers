from .AllRecipes import AllRecipes
from .BBCCoUk import BBCCoUk
from ._result import SearchResult
from typing import List

SEARCHERS = {
    AllRecipes.host() : AllRecipes,
    BBCCoUk.host() : BBCCoUk
}

def search_recipe(keyword : str) -> SearchResult:
    results : SearchResult = SearchResult(keyword)
    for key in SEARCHERS:
        searcher = SEARCHERS[key]
        result = searcher().search(keyword)
        results = results.merge(result)

    return results

__all__ = ["search_recipe"]
name = "recipe_searchers"