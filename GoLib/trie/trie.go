package main

import (
	"C"
	"log"
)

type TrieNode struct {
	Dic    map[string]TrieNode
	IsLeaf bool
}

type Trie struct {
	Dic map[string]TrieNode
}

func (trie Trie) Add(keyword string) {

	dic := trie.Dic

	r := []rune(keyword)
	for i := 0; i < len(r); i = i + 1 {

		char := string(r[i])

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
	r := []rune(letter)
	for i := 0; i < len(r); i = i + 1 {

		char := string(r[i])
		pattern += char

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
			Dic:    make(map[string]TrieNode),
			IsLeaf: true,
		}
	} else {
		nextChar := string(subStr[1])
		nextNode := toTrieNode(subStr[1:])

		dic := make(map[string]TrieNode)
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
		Dic: make(map[string]TrieNode),
	}

	log.Println("trie initialized!")
}

func AddKeyword(keyword string) {
	trie.Add(keyword)
}

func MatchLetter(letter string) string {
	return trie.Match(letter)
}

func main() {

}
