
class TrieNode:
    def __init__(self, dic, isLeaf):
        self.Dic = dic
        self.IsLeaf = isLeaf


class Trie:
    def __init__(self):
        self.Dic = {}


    def Add(self, keyword):
        if len(keyword) == 0: return

        dic = self.Dic
        for i in range(len(keyword)):
            char = keyword[i]
            if char in dic:
                dic = dic[char].Dic # if the char is already in the dic, we go for the next char
            else:
                # if the char doesn't exist, it's created to the found dic
                dic[char] = self.toTrieNode(keyword[i:])
                return


    def Match(self, string):
        pattern = ""

        dic = self.Dic # starting from the root node
        for i in range(len(string)):
            char = string[i]
            pattern += char

            if char in dic:
                node = dic[char]
                if node.IsLeaf:
                    return pattern # if this the leaf, meaning all chars are matched now
                else:
                    dic = node.Dic # keep comparing
            else:
                return "" # not found

        return "" # end of the word is reached before the whole pattern matches


    # ----------------------------------------- Private Methods

    def toTrieNode(self, string):
        # this will create a node for each char: a link to the next node

        if len(string) == 1:
            return TrieNode({}, True)  # a node as the leaf with an empty dictionary
        else:
            nextChar = string[1]
            nextNode = self.toTrieNode(string[1:])
            return TrieNode({nextChar: nextNode}, False)  # link to the next char



# driver code:
# trie = Trie()
# trie.Add("this")
# trie.Add("think")
# trie.Add("thought")
# trie.Add("narrow")
# trie.Add("nudge")
# trie.Add("pair")

# print("his: " + str(trie.Match("his")))
# print("thinks: " + str(trie.Match("thinks")))
# print("though: " + str(trie.Match("though")))
# print("pair: " + str(trie.Match("pair")))


# result:
# his:
# thinks: think
# though:
# pair: pair