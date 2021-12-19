
import ctypes

library = ctypes.cdll.LoadLibrary('./bin/trie.so')
Initialize_Trie = library.InitializeTrie
Initialize_Trie()


Add_Keyword = library.AddKeyword
Add_Keyword("asdad")

Match_Letter = library.MatchLetter
Match_Letter.argtypes = [ctypes.c_char_p]
Match_Letter.restype = ctypes.c_void_p
ptr = Match_Letter('as'.encode('utf-8'))
out = ctypes.string_at(ptr)

print(out.decode('utf-8'))