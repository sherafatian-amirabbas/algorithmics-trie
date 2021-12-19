import ctypes
from pathlib import Path

root_path = str(Path(__file__).parent.parent)
bin_path = root_path + '\\bin'

GoLib = ctypes.cdll.LoadLibrary(f'{bin_path}/trie.so')

Initialize_Trie = GoLib.InitializeTrie
Add_Keyword = GoLib.AddKeyword
Match_Letter = GoLib.MatchLetter


def TrieInitialize():
    Initialize_Trie()

def Add(keyword):
    Add_Keyword.argtypes = [ctypes.c_char_p]
    Add_Keyword(keyword.encode('utf-8'))

def Match(letter):
    Match_Letter.argtypes = [ctypes.c_char_p]
    Match_Letter.restype = ctypes.c_void_p
    ptr = Match_Letter(letter.encode('utf-8'))
    out = ctypes.string_at(ptr)
    return out.decode('utf-8')
