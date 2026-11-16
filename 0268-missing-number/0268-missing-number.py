class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total_sum=n*((n+1))/2
        arr_sum=sum(nums)
        return total_sum-arr_sum