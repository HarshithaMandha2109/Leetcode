class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(nums,target):
            left=-1
            n=len(nums)
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    left=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return left
        def last(nums,target):
            right=-1
            n=len(nums)
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    right=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return right
        left=first(nums,target)
        right=last(nums,target)

        return [left,right]
        