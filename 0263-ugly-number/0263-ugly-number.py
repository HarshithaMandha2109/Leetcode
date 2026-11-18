class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        p_f=[2,3,5]
        for i in p_f:
            while n%i==0:
                n//=i
        return n==1
            