class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        window_sum = 0
        ans = 1

        for right in range(len(nums)):

            window_sum += nums[right]

            while nums[right] * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

# T: O(n log n)
# S: O(1) extra space (algorithm variables)