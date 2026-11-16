class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=0
        if x<0:
            n=True
        else:
            n=False
        x=abs(x)
        while x>0:
            last=x%10
            ans=ans*10+last
            x//=10
        if n:
            ans=-ans
        if -2**31<ans and ans<2**31-1:
            return ans
        return 0
    