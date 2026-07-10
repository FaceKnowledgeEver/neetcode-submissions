class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    #     d1 = self.hashmap(s)
    #     d2 = self.hashmap(t)
    #     if d1 == d2:
    #         return True
    #     else:
    #         return False

    # def hashmap(self, string : str) -> dict:
    #     s = set()
    #     d = {}
    #     for c in string:
    #         if c not in s:
    #             s.add(c)
    #             d[c] = 1
    #         else:
    #             d[c] += 1
    #     return d
        
