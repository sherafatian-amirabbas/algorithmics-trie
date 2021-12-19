package main

import (
	"C"
	// "fmt"
	// pkg "github.com/algorithmics-trie/GoLib/trie"
)

func main() {

	var a *C.char = C.CString("text")

	b := C.GoString(a)

	print(a)
	print(b)

	// driver code

	// trie := pkg.Trie{
	// 	Dic: make(map[byte]pkg.TrieNode),
	// }

	// trie.Add("this")
	// trie.Add("think")
	// trie.Add("thought")
	// trie.Add("narrow")
	// trie.Add("nudge")
	// trie.Add("pair")

	// fmt.Println("his: " + trie.Match("his"))
	// fmt.Println("thinks: " + trie.Match("thinks"))
	// fmt.Println("though: " + trie.Match("though"))
	// fmt.Println("pair: " + trie.Match("pair"))

	// result:
	// his:
	// thinks: think
	// though:
	// pair: pair
}
