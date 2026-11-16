class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        k=0
        for i in range(k+1,n):
            if nums[k]!=nums[i]:
                k+=1
                nums[k],nums[i]=nums[i],nums[k]
        return k+1