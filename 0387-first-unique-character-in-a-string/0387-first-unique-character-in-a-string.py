class Solution:
    def firstUniqChar(self, s: str) -> int:
        h=Counter(s)
        for i,j in h.items():
            if j==1:
                return s.index(i)
        return -1