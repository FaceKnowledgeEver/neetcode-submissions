from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # values_selected = []
        # most_commons = Counter(nums).most_common()
        # for m in range(k):
        #     values_selected.append(most_commons[m][0])
        # return values_selected
        return [val for val, _ in Counter(nums).most_common(k)]