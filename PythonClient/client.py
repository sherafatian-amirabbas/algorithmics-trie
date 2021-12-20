import sys
import TrieBridge
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
TrieBridge.TrieInitialize()


# feeding trie
keywords = fileReader.getListOfWords(assets_path, "keywords-mini.txt")
for pattern in keywords:
    TrieBridge.Add(pattern)


# reading text file
text = fileReader.getText(assets_path, "book-mini.txt")


# function of seeking for patterns
@profile
def get_matched_keywords(text):
    matchedKeywords = []
    for i in range(len(text)):
        string = text[i:]
        keyword = TrieBridge.Match(string)
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
# print(matchedKeywords)
print("\nexectime: " + str(exectime))


# result for mini version
# exectime: 212.020751953125
# exectime: 175.001953125 => when C.cstring is ignored

# result for full version
# exectime: 375297.314453125