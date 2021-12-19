import TrieBridge
from pathlib import Path
import sys

root_path = str(Path(__file__).parent.parent)
bin_path = root_path + '\\bin'
sys.path.append(bin_path)

import monitor



monitor.start()

TrieBridge.TrieInitialize()
TrieBridge.Add('bananna')
TrieBridge.Add('pan')
TrieBridge.Add('and')
TrieBridge.Add('nab')
TrieBridge.Add('antenna')
TrieBridge.Add('bandana')
TrieBridge.Add('ananas')
TrieBridge.Add('ananas')
TrieBridge.Add('nana')


text = "panamabananas"
matchedKeywords = []
for i in range(len(text)):
    string = text[i:]
    keyword = TrieBridge.Match(string)
    if keyword != "":
        matchedKeywords.append(keyword)

execTimeInMS = monitor.end()

print("ExecTime: " + str(execTimeInMS))
print(matchedKeywords)
