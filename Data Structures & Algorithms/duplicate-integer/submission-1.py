from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        if 0 <= len(nums) <= 10**5:
            for num in nums :
                if num in hashset:
                    return True
                hashset.add(num)
        return False

