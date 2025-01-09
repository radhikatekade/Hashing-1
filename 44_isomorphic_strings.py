# Time complexity - O(n)
# Space complexity - O(1) # since length can be 52 chars max - upper + lowercase case

# Approach - Maintain a hashmap for str s and a set for str t
# If a char exists in smap, check if its value is equal to existing value, else return False
# If char already exists in tset, return False 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_set = set()

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i]
                if t[i] not in t_set:
                    t_set.add(t[i])
                else:
                    return False
            else:
                if s_map[s[i]] != t[i]:
                    return False
        
        return True