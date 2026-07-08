class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        ans = float('inf')

        for right in range(len(nums)):

            window_sum += nums[right]

            while window_sum >= target:
                ans = min(ans, right - left + 1)
                
                window_sum -= nums[left]

                left += 1

        if ans == float('inf'):
            return 0

        return ans