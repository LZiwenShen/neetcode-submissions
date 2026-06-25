class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = 0
        cnt = set()
        mx = 0
        for right in range(len(s)):
            while s[right] in cnt:
                cnt.remove(s[left])
                left += 1
            cnt.add(s[right])
            mx = max(mx, right - left + 1)
        return mx