# Time complexity - O(n)
# Space complexity - O(n)

# Approach - Maintain two hashmaps that maps from char to word and word to char and if the mapping fail in
# either of the maps, return False.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        c_to_w = {}
        w_to_c = {}
        for i in range(len(words)):
            char = pattern[i]
            word = words[i]
            if char in c_to_w and c_to_w[char] != word:
                return False
            if word in w_to_c and w_to_c[word] != char:
                return False
            c_to_w[char] = word
            w_to_c[word] = char
        return True