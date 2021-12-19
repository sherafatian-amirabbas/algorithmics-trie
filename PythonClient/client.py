
import ctypes

library = ctypes.cdll.LoadLibrary('./bin/trie.so')
Initialize_Trie = library.InitializeTrie
Initialize_Trie()
