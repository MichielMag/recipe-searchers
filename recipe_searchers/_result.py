from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class RecipeLink:
    title: str
    url: str
    website: str

@dataclass
class SearchResult:
    keyword : str
    results : Dict[str, List[RecipeLink]] 
    count : int

    def __init__(self, keyword : str, result : Dict[str, List[RecipeLink]] = {}):
        self.keyword = keyword
        self.results = result
        self.count = self.length
    
    def merge(self, result : SearchResult) -> Dict[str, List[RecipeLink]]:
        """ A function that makes sure the SearchResults are immutable. This function makes a new SearchResult with both results merged. """
        new_dict : Dict[str, List[RecipeLink]] = {}
        # Go through all own results and merge them with other
        for key in self.results:
            new_dict[key] = self.results[key]
            if key in result.results.keys():
                new_dict[key] = new_dict[key] + result.results[key]
        
        # And the other way around.
        for key in result.results:
            if key not in new_dict.keys():
                new_dict[key] = result.results[key]
        
        # return a new result, making this one immutable.
        new_result = SearchResult(self.keyword, new_dict)

        return new_result
    
    @property
    def length(self):
        """ Counts all the elements in the dictionary for every key """
        return sum([len(elements) for elements in self.results.values()])