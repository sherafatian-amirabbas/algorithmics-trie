package main

import (
	"fmt"

	"github.com/algorithmics-trie/GoLib/trie"
)

func main() {

	// driver code

	trie.InitializeTrie()

	trie.AddKeyword("this")
	trie.AddKeyword("think")
	trie.AddKeyword("thought")
	trie.AddKeyword("narrow")
	trie.AddKeyword("nudge")
	trie.AddKeyword("pair")

	fmt.Println("his: " + trie.MatchLetter("his"))
	fmt.Println("thinks: " + trie.MatchLetter("thinks"))
	fmt.Println("though: " + trie.MatchLetter("though"))
	fmt.Println("pair: " + trie.MatchLetter("pair"))

	// result:
	// his:
	// thinks: think
	// though:
	// pair: pair
}
