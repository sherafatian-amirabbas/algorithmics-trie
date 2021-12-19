from Trie import Trie
from pathlib import Path
import sys

root_path = str(Path(__file__).parent.parent)
assets_path = root_path + '\\Assets'
bin_path = root_path + '\\bin'
sys.path.append(bin_path)

import monitor
import fileReader


trie = Trie()


# feeding trie
keywords = fileReader.getListOfWords(assets_path, "keywords-mini.txt")
for pattern in keywords:
    trie.Add(pattern)


# reading text file
text = fileReader.getText(assets_path, "book-mini.txt")


monitor.start()


# seeking for patterns
matchedKeywords = []
for i in range(len(text)):
    string = text[i:]
    keyword = trie.Match(string)
    if keyword != "":
        matchedKeywords.append(keyword)


execTimeInMS = monitor.end()


# printing out the result
print(matchedKeywords)
print("\nExecTime: " + str(execTimeInMS))


# result: ExecTime: 61.998779296875