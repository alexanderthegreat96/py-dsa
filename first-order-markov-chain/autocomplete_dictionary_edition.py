# the premise of solving auto-complete
# this will most likely guarantee O(1)
# since we are going to index each word
# and combinations this way
# the first string is the key, whatever else follows,
# will be the values
# example input:
# [
#   ["i", "will", "be", "there"],
#   ["i", "am", "you", "are"]
# ]

from collections import defaultdict, Counter
from typing import List

class AutoComplete:
    def __init__(self) -> None:
        # a word is getting mapped to a counter
        # example: self.model["i"] = Counter({"am": 1, "will": 1, "like": 1})
        self.model: defaultdict = defaultdict(Counter)
    
    def train(self, sentences: List[List[str]]) -> None:
        """Processes nested lists to learn word transitions."""
        for sentence in sentences:
            # we grab words in pairs
            # word[i] and word[i + 1]
            for i in range(len(sentence) - 1):
                curr_word = sentence[i]
                next_word = sentence[i+1]
                self.model[curr_word][next_word] += 1
    
    def predict(self, current_word: str, limit: int = 5) -> List[str]:
        """Predicts the most likely next words based on training data."""
        if current_word not in self.model:
            return []
        
        # frequency data
        # should return something in the lines of: [('am', 5), ('will', 3), ('like', 2)]
        raw_suggestions = self.model[current_word].most_common(limit)

        # word extraction, nothing fancy here
        suggestions = []
        for word, count in raw_suggestions:
            suggestions.append(word)
            
        return suggestions 

# running manual tests
# google's own input here
input_data: List[List[str]] = [
    ["i", "am", "here", "you"],
    ["i", "will", "be", "there"],
    ["i", "like", "breads", "and", "butter"],
    ["i", "will", "always", "love", "coding"]
]

autocomplete = AutoComplete()
autocomplete.train(input_data)

print(f"Next word after 'i': {autocomplete.predict('i')}")
print(f"Next word after 'will': {autocomplete.predict('will')}")
print(f"Next word after 'breads': {autocomplete.predict('breads')}")