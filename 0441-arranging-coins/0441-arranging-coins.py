class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        ans=0
        while low<=high:
            mid=(low+high)//2
            n_c=mid*(mid+1)/2
            if n_c<=n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans