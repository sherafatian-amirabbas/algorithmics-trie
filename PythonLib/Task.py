import sys
from Trie import Trie
from pathlib import Path
from memory_profiler import profile

# root_path for jeyhun
root_path = '..\\'                              

# root_path for amir
# root_path = str(Path(__file__).parent.parent)

# set assets and import bin
assets_path = root_path + '\\Assets'
bin_path = root_path + '\\bin'
sys.path.append(bin_path)

import monitor
import fileReader


# trie initialization
trie = Trie()


# feeding trie
keywords = fileReader.getListOfWords(assets_path, "keywords-mini.txt")
for pattern in keywords:
    trie.Add(pattern)


# reading text file
text = fileReader.getText(assets_path, "book-mini.txt")


# function of seeking for patterns
@profile
def get_matched_keywords(text):
    matchedKeywords = []
    for i in range(len(text)):
        string = text[i:]
        keyword = trie.Match(string)
        if keyword != "":
            matchedKeywords.append(keyword)
    return matchedKeywords


# start timer
monitor.start()

# seeking for patterns
matchedKeywords = get_matched_keywords(text)

# stop timer
exectime = monitor.end()


# printing out the result
#print(matchedKeywords)
print("\nexectime: " + str(exectime))


# result for mini version
# exectime: 61.998779296875

# result for full version
# exectime: 75685.92797851562