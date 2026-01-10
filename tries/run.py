import readchar
import sys
from tries import Trie
from typing import Optional

# simple enough
# takes an instance of trie
# and inserts the words from the text file
# then returns the object
def load_words_into_trie(trie: Trie)  -> Optional[Trie]:
    try:
        with open("words/words_alpha.txt", "r") as f:
            for line in f:
                word = line.strip()
                trie.insert(word.lower())

            return trie
    except Exception as e:
        print(f'something went wrong: {e}')
        return

# nifty little UI / CLI trick to emulate realtime searching
def render_ui(query : Optional[str], suggestions : Optional[list]) -> None:
    if not query or not suggestions:
        return
    
    sys.stdout.write("\r" + "\033[K") 
    sys.stdout.write(f"Search: {query}\n")
    
    display_count = 5
    for i in range(display_count):
        if i < len(suggestions):
            sys.stdout.write(f"\033[K  > {suggestions[i]}\n")
        else:
            sys.stdout.write("\033[K\n") # Clear empty slots
            
    sys.stdout.write(f"\033[{display_count + 1}A") 
    sys.stdout.write(f"\rSearch: {query}")
    sys.stdout.flush()

def main():
    init = Trie()
    trie : Optional[Trie] = load_words_into_trie(init)
    if not trie:
        return
    
    query = ""
    print("Trie Auto-Complete (Googler's Edition) (Press 'Ctrl+C' to exit)")
    print("Type something: ", end="", flush=True)

    while True:
        char = readchar.readkey()

        if char == readchar.key.CTRL_C:
            break
        elif char in (readchar.key.BACKSPACE, '\x7f'):
            query = query[:-1]
        elif len(char) == 1:
            query += char

        suggestions = trie.suggest(query.lower())
        render_ui(query, suggestions[:5])

if __name__ == "__main__":
    main()