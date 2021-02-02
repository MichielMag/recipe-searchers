from .AllRecipes import AllRecipes
from .BBCCoUk import BBCCoUk
from .BBCGoodFood import BBCGoodFood
from .BonAppetit import BonAppetit
from .TheWoksOfLife import TheWoksOfLife
from .HostTheToast import HostTheToast
from .JamieOliver import JamieOliver
from .NyTimes import NyTimes
from .Food import Food
from ._result import SearchResult, RecipeLink
from typing import List
from ._logger import Logger

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

available_searchers = list(SEARCHERS.keys())

def search_recipe(keyword : str, 
                  verbose : bool = False,
                  limit_per_searcher : int = -1,
                  limit_to_searchers : List[str] = []) -> SearchResult:
    # We're using Logger as a static class.
    Logger.verbose = verbose

    if limit_per_searcher > 0:
        Logger.info(f'Going to search for {keyword}, limitting to {limit_per_searcher} searchers per searcher')
    else:
        Logger.info(f'Going to search for {keyword}')
    
    results : SearchResult = SearchResult(keyword)

    if len(limit_to_searchers) == 0:
        limit_to_searchers = SEARCHERS.keys()

    # Call search for every searcher and merge each result.
    for searcher in limit_to_searchers:
        if SEARCHERS[searcher] is not None:
            result = SEARCHERS[searcher]().search(keyword, limit_per_searcher)
            results = results.merge(result)

    return results

__all__ = ["search_recipe", "available_searchers", "SearchResult", "RecipeLink"]
name = "recipe_searchers"