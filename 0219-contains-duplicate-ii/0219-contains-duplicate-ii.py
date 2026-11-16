class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] in d:
                if abs(d[nums[i]]-i)<=k:
                    return True
            d[nums[i]]=i
        return False