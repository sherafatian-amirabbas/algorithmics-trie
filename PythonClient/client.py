
import ctypes

library = ctypes.cdll.LoadLibrary('./bin/trie.so')

def TrieInitialize():
    Initialize_Trie = library.InitializeTrie
    Initialize_Trie()

def Add(keyword):
    Add_Keyword = library.AddKeyword
    Add_Keyword.argtypes = [ctypes.c_char_p]
    Add_Keyword(keyword.encode('utf-8'))

def Match(letter):
    Match_Letter = library.MatchLetter
    Match_Letter.argtypes = [ctypes.c_char_p]
    Match_Letter.restype = ctypes.c_void_p
    ptr = Match_Letter(letter.encode('utf-8'))
    out = ctypes.string_at(ptr)
    return out.decode('utf-8')


TrieInitialize()
Add('bananna')
Add('pan')
Add('and')
Add('nab')
Add('antenna')
Add('bandana')
Add('ananas')
Add('ananas')
Add('nana')

text = "panamabananas"
matchedKeywords = []
for i in range(len(text)):
    string = text[i:]
    keyword = Match(string)
    if keyword != "":
        matchedKeywords.append(keyword)

print(matchedKeywords)
