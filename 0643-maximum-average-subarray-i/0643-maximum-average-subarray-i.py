class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = 0
        max_sum = float('-inf')

        for right in range(len(nums)):

            window_sum += nums[right]

            if right - left + 1 > k:

                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:

                max_sum = max(max_sum, window_sum)

        return max_sum / k

# T: 0(n), S: 0(1)