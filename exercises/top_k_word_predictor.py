class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the top suggestions passing through this node
        # Format: [(word, frequency), ...]
        self.suggestions = []

class WordPredictor:
    def __init__(self, top_k=3):
        self.root = TrieNode()
        self.top_k = top_k

    def insert(self, word, frequency):
        """Adds a word to the Trie and updates suggestions at each node."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            # Update the suggestions list for this prefix
            # 1. Add/Update the current word's frequency
            node.suggestions.append((word, frequency))
            # 2. Sort by frequency (descending) and keep only top_k
            node.suggestions.sort(key=lambda x: x[1], reverse=True)
            
            # Remove duplicates of the same word if updated
            seen = set()
            new_suggestions = []
            for w, f in node.suggestions:
                if w not in seen:
                    new_suggestions.append((w, f))
                    seen.add(w)
            node.suggestions = new_suggestions[:self.top_k]

    def predict(self, prefix):
        """Returns the top_k words for a given prefix in O(Length of Prefix)."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No matches found
            node = node.children[char]
        
        return [word for word, freq in node.suggestions]

# --- Testing the Predictor ---
predictor = WordPredictor(top_k=3)
data = [("apple", 50), ("app", 100), ("apply", 75), ("ball", 200), ("ape", 10)]

for word, freq in data:
    predictor.insert(word, freq)

print(f"Predictions for 'ap': {predictor.predict('ap')}") 
# Output: ['app', 'apply', 'apple'] (Sorted by frequency)