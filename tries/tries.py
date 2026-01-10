# In computer science, a trie also known as a digital tree or prefix tree, is a specialized search tree data structure
# used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. 
# Instead, each node's position within the trie determines its associated key, 
# with the connections between nodes defined by individual characters rather than the entire key.

# common uses: dictionaries, word completion, word suggestion
# tries are also known as prefix trees

# a little note from me
# in a google interview I was asked this question
# and to be honest, I was thinking I could solve this using hashmaps
# and you definately can, but, they were expecting tree prefixes
# although, I am unsure you can write all of this code
# and expect it to work without executing, since the logic is a bit twisted
# I wrote this afterwards, scratching my head

from typing import Optional, List
 
class Node:
    def __init__(self):
        self._children : List[Optional[Node]] = [None] * 26
        self._is_end_of_word : bool = False
    
    def get_child(self, idx : int) -> "Node | None":
        return self._children[idx]
    
    def set_child(self, idx: int, node: Optional["Node"]) -> None:
        self._children[idx] = node
    
    def set_is_end_of_word(self, value: bool) -> None:
        self._is_end_of_word = value
    
    def get_is_end_of_word(self) -> bool:
        return self._is_end_of_word
    
    def get_children(self) -> List[Optional["Node"]]:
        return self._children

class Trie:
    def __init__(self) -> None:
        self.root = Node()
        
    # hash function or sort of
    def char_to_index(self, char : str) -> int:
        return ord(char) - ord('a')
    
    # just insert
    def insert(self, word : str) -> None:
        if not word:
            return
        
        node = self.root
        for char in word:
            idx = self.char_to_index(char)
            child = node.get_child(idx)
            if child is None:
                child = Node()
                node.set_child(idx, child)
            node = child
            
        node.set_is_end_of_word(True)  
    
    # this is gonna fry your brain
    def delete(self, node: Node, word: str, depth: int = 0) -> bool:
        if node is None:
            return False  # word not found

        # we're at the last char
        if depth == len(word):
            if not node.get_is_end_of_word():
                return False  # word not found
            node.set_is_end_of_word(False)

            # if no children found, then delete
            return all(child is None for child in node.get_children())

        idx : int = self.char_to_index(word[depth])
        child = node.get_child(idx)
        if child is None:
            return False  # nothing found

        should_delete_child = self.delete(child, word, depth + 1)

        # if true, delete the children refferences
        if should_delete_child:
            node.set_child(idx , None)
            # return True if this node has no children and is not end of another word
            return not node.get_is_end_of_word() and all(c is None for c in node.get_children())

        return False
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = self.char_to_index(char)
            child = node.get_child(idx)
            if child is None:
                return False  # word not found
            node = child
        return node.get_is_end_of_word()
    
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = self.char_to_index(char)
            child = node.get_child(idx)
            if child is None:
                return False
            node = child
        return True

    # uses spaces to perform multiple operations
    # it will not work as reliably
    # considering that we are definately dealing with
    # a situation where a trie is used to index single
    # words and the inputs should be cascaded and then merged
    # aka: you type a word, a suggestion pops, you select that suggestion
    # and then another suggestion pops
    def suggest(self, prefix: str) -> List[str]:
        node = self.root
        words = prefix.split(" ")

        for word in words:
            for char in word:
                idx = self.char_to_index(char)
                child = node.get_child(idx)
                if child is None:
                    return []  # no prefix found
                node = child

        # full prefix
        full_prefix = " ".join(words[:-1])
        if full_prefix:
            full_prefix += " "
        last_word_prefix = words[-1]
        path = full_prefix + last_word_prefix

        suggestions: List[str] = []
        self._collect_words(node, path, suggestions)
        return suggestions
 
    # this collects words from a node
    # based on the hashed prefix
    def _collect_words(self, node: Node, path: str, output: List[str]) -> None:
        if node.get_is_end_of_word():
            output.append(path)

        for idx, child in enumerate(node.get_children()):
            if child is not None:
                char = chr(idx + ord('a'))
                self._collect_words(child, path + char, output)
                