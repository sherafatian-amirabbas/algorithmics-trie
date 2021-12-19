import TrieBridge
from pathlib import Path
import sys

root_path = str(Path(__file__).parent.parent)
assets_path = root_path + '\\Assets'
bin_path = root_path + '\\bin'
sys.path.append(bin_path)

import monitor
import fileReader




# trie initialization
TrieBridge.TrieInitialize()


# feeding trie
keywords = fileReader.getListOfWords(assets_path, "keywords.txt")
for pattern in keywords:
    TrieBridge.Add(pattern)


# reading text file
text = fileReader.getText(assets_path, "book.txt")


monitor.start()


# seeking for patterns
matchedKeywords = []
for i in range(len(text)):
    string = text[i:]
    keyword = TrieBridge.Match(string)
    if keyword != "":
        matchedKeywords.append(keyword)


execTimeInMS = monitor.end()


# printing out the result
print(matchedKeywords)
print("\nExecTime: " + str(execTimeInMS))


# result for mini version
# ExecTime: 212.020751953125
# ExecTime: 175.001953125 => when C.cstring is ignored

# result for full version
# ExecTime: 375297.314453125