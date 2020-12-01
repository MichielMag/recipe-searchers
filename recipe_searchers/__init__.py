from .AllRecipes import AllRecipes
from .BBCCoUk import BBCCoUk
from .BBCGoodFood import BBCGoodFood
from .BonAppetit import BonAppetit
from .TheWoksOfLife import TheWoksOfLife
from .HostTheToast import HostTheToast
from .JamieOliver import JamieOliver
from .NyTimes import NyTimes
from .Food import Food
from ._result import SearchResult
from typing import List

SEARCHERS = {
    AllRecipes.host() : AllRecipes,
    BBCCoUk.host() : BBCCoUk,
    BBCGoodFood.host() : BBCGoodFood,
    BonAppetit.host() : BonAppetit,
    TheWoksOfLife.host() : TheWoksOfLife,
    Food.host() : Food,
    HostTheToast.host() : HostTheToast,
    JamieOliver.host() : JamieOliver,
    NyTimes.host() : NyTimes
}

def search_recipe(keyword : str) -> SearchResult:
    results : SearchResult = SearchResult(keyword)
    for searcher in SEARCHERS:
        result = SEARCHERS[searcher]().search(keyword)
        results = results.merge(result)

    return results

__all__ = ["search_recipe"]
name = "recipe_searchers"