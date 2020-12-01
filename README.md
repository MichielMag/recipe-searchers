# recipe-searchers
A simple web scraping tool for searching for recipe links, inspired by (and possibly for use with) [recipe-scapers](https://github.com/hhursev/recipe-scrapers).

## To install
```
pip install recipe_searchers
```

## To use
```python
from recipe_searchers import search_recipe

result = search_recipe("panna cotta")
print(f"Found results: \n {result}")
```
```search_recipe()``` returns an object in the form of:

```python
@dataclass
class SearchResult:
    keyword : str
    # str = website, List = results
    results : Dict[str, List[RecipeLink]]
```

Where results is a pair of Website for every website it has found results and a list of results.

## Searchers available for:
- [allrecipes.com](https://allrecipes.com)
- [bbc.co.uk](https://www.bbc.co.uk/food/)
- [bbcgoodfooc.com](https://www.bbcgoodfood.com/)
- [bonappetit.com](https://www.bonappetit.com/)