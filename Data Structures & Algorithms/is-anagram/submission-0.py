from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        counter_s = Counter(s).most_common()
        counter_s.sort()
        counter_t = Counter(t).most_common()
        counter_t.sort()
        if counter_s == counter_t :
            return True
        return False  