class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=-1
        last=-1
        l=0
        r=len(nums)-1
        s=0
        e=len(nums)-1 
        while l<=r:
            m=(l+r)// 2
            if nums[m]==target:
                first=m
                r=m-1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        while s<=e:
            m =(s+e)// 2
            if nums[m]==target:
                last=m
                s=m+1
            elif nums[m]>target:
                e= m-1
            else:
                s=m+1
        return [first, last]
