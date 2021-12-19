
import ctypes

library = ctypes.cdll.LoadLibrary('./trie.so')
Initialize_Trie = library.InitializeTrie
Initialize_Trie()
