class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target-n
            print(diff)
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
            print(prevMap)
        # for i in range(len(nums)-1) :
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i]+nums[j]
        #         if sum == target:
        #             return [i,j]
