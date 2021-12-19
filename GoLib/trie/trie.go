package main

import (
	"C"
)

type TrieNode struct {
	Dic    map[byte]TrieNode
	IsLeaf bool
}

type Trie struct {
	Dic map[byte]TrieNode
}

func (trie Trie) Add(keyword string) {

	dic := trie.Dic

	for i := 0; i < len(keyword); i = i + 1 {

		char := keyword[i]

		node, isFound := dic[char]
		if isFound {
			// if the char is already in the dic, we go for the next char
			dic = node.Dic
		} else {
			// if the char doesn't exist, it's created to the found dic
			dic[char] = toTrieNode(keyword[i:])
			return
		}
	}
}

func (trie Trie) Match(letter string) string {
	pattern := ""

	dic := trie.Dic
	for i := 0; i < len(letter); i = i + 1 {

		char := letter[i]
		pattern += string(char)

		node, isFound := dic[char]
		if isFound {
			if node.IsLeaf {
				return pattern // if this the leaf, meaning all chars are matched now
			} else {
				dic = node.Dic // keep comparing
			}
		} else {
			return "" // not found
		}
	}

	return "" // end of the word is reached before the whole pattern matches
}

// ----------------------------------------- Private Methods

func toTrieNode(subStr string) TrieNode {
	// this will create a node for each char: a link to the next node

	if len(subStr) == 1 {
		// a node as the leaf with an empty dictionary
		return TrieNode{
			Dic:    make(map[byte]TrieNode),
			IsLeaf: true,
		}
	} else {
		nextChar := subStr[1]
		nextNode := toTrieNode(subStr[1:])

		dic := make(map[byte]TrieNode)
		dic[nextChar] = nextNode

		return TrieNode{
			Dic:    dic,
			IsLeaf: false,
		}
	}
}

// ----------------------------------------- Public Methods

var trie Trie

//export InitializeTrie
func InitializeTrie() {
	trie = Trie{
		Dic: make(map[byte]TrieNode),
	}
}

//export AddKeyword
func AddKeyword(keyword *C.char) {
	keyword_go := C.GoString(keyword)
	trie.Add(keyword_go)
}

//export MatchLetter
func MatchLetter(letter *C.char) *C.char {
	letter_go := C.GoString(letter)
	match_go := trie.Match(letter_go)
	return C.CString(match_go)
}

func main() {
}
