

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagram:
                anagram[key] = [s]
            else:
                anagram[key].append(s)
        return anagram.values()
            
            
Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])    
        
        