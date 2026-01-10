from typing import Optional, Any


# the premise of solving auto-complete
# this will most likely guaranyee O(1)
# since we are going to index each word
# and combinations this way
# the first string is the key, whatever else follows,
# will be the values
# example input:
# [
#   ["i", "will", "be", "there"],
#   ["i", "am", "you", "are"]
# ]

class AutoComplete:
    def __init__(self) -> None:
        ...
    
    def train(self, words : list[list[str]]) -> None:
        word_count: dict = {} 
        for sentence in words:
            for word in sentence:
                word_count[word] = word_count.get(word, 0) + 1
        
        for word, count in word_count.items():
            pass
    
    def predict(self, input : Optional[str]) -> Optional[list[str]]:
        pass

input_data : list[list[str]] = [
    ["i", "am", "here", "you"],
    ["i", "will", "be", "there"],
    ["i", "like", "breads", "and", "butter"]
]

autocomplete : AutoComplete = AutoComplete()
autocomplete.train(input_data)