class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        mx_cnt = 0
        mx_len = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            mx_cnt = max(mx_cnt, cnt[s[r]])
            while r - l + 1 - mx_cnt > k:
                cnt[s[l]] -= 1
                l += 1
            mx_len = max(mx_len, r - l + 1)
        return mx_len