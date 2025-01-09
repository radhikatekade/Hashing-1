# Time complexity - O(nklogk) n = len(strs), k = len(str), klogk because of sorting
# Space complexity - O(nk)

# Approach - maintain a map whose key is a sorted list of chars of str and whose value is a list
# of all strings that match that key once sorted

# from typing import List
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         str_map = {}

#         for st in strs:
#             sorted_str = tuple(sorted(st))
#             if sorted_str not in str_map:
#                 str_map[sorted_str] = []
#             str_map[sorted_str].append(st)
        
#         return list(str_map.values())

# more efficient approach - prime product
# Time complexity - O(nk)
# Space complexity - O(nk)

# Now key of the map is prime product instead of sorted chars

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for st in strs:
            prime_prod = self.primeProduct(st)
            if prime_prod not in str_map:
                str_map[prime_prod] = []
            str_map[prime_prod].append(st)
        
        return list(str_map.values())
    
    def primeProduct(self, st: str) -> int:
        primes = [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
        79, 83, 89, 97, 101, 103]

        prod = 1
        for i in st:
            prod *= primes[ord(i) - ord("a")]
        
        return prod