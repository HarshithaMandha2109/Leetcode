class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        se=set()
        maxi=0
        for right in range(n):
            while s[right] in se:
                se.remove(s[left])
                left+=1
            se.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi


        