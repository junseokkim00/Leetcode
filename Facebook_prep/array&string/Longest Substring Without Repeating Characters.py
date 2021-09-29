class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        count=0;
        Set=set()
        for j in range(len(s)):
            count=0
            Set.clear()
            for i in s[j:]:
                if i not in Set:
                    Set.add(i)
                    count+=1
                else:
                    break
                res = max(res,count)
        return res


# Sliding Windows
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


# Sliding Windows Optimized(with Hashmap)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans