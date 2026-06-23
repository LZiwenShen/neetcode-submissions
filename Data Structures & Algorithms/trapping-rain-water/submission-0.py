class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        pre_max, suf_max = 0, 0
        ans = 0
        while l < r:
            pre_max = max(height[l], pre_max)
            suf_max = max(height[r], suf_max)
            if pre_max < suf_max:
                ans += pre_max - height[l]
                l += 1
            else:
                ans += suf_max - height[r]
                r -= 1
        return ans