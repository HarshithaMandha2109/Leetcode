class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        h={}
        for i in range(n):

                number=target-nums[i]
                if number in h:
                    return i,h[number]
                h[nums[i]]=i
                  
                