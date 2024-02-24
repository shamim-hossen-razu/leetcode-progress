class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        temp_str = ''
        max_str = ''
        if s == s[::-1]:
            return s
        else:
            for i in range (0, len(s)):
                match_list = []
                for j in range (i, len(s)):
                    if s[j] == s[i]:
                        match_list.append(j)
                if len(match_list) > 0:
                    for item in match_list:
                        temp_str = s[i: item + 1]
                        if temp_str == temp_str[::-1]:
                            if len(temp_str) > max_length:
                                max_length = len(temp_str)
                                max_str = temp_str
                i += 1
            return max_str