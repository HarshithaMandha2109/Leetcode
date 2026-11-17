# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        ans=0
        while low<=high:
            mid=(low+high)//2
            val=isBadVersion(mid)
            if val:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans