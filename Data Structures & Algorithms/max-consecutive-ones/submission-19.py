class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, n = 0, len(nums)
        for i in range(n):
            sum_ones = 0
            for j in range(i, n):
                if nums[j] == 0: break
                sum_ones +=1
            max_ones= max(sum_ones, max_ones)
        return max_ones
