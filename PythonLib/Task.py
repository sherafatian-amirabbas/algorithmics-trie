from Trie import Trie


trie = Trie()
trie.Add('bananna')
trie.Add('pan')
trie.Add('and')
trie.Add('nab')
trie.Add('antenna')
trie.Add('bandana')
trie.Add('ananas')
trie.Add('ananas')
trie.Add('nana')

text = "panamabananas"
matchedKeywords = []
for i in range(len(text)):
    string = text[i:]
    keyword = trie.Match(string)
    if keyword != "":
        matchedKeywords.append(keyword)

print(matchedKeywords)


# result
# ['pan', 'ananas', 'nana']