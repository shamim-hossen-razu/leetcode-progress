class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        for i in range(0, len(s)):
            temp = []
            counter = 0
            temp.append(s[i])
            counter += 1
            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                    counter += 1
                else:
                    i += 1
                    break
            if counter > longest_substring:
                longest_substring = counter
                    
        return longest_substring
    
print(Solution().lengthOfLongestSubstring("abcabcbb")) 




                    

            
            

