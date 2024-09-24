from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) ==1:
            return nums[left]
        mid = left + (right - left)//2
        while left < right :
            mid = left + (right - left)//2
            if nums[left] < nums[right] :
                return nums[left]
            elif nums[right] < nums[right-1] :
                return nums[right]
            elif nums[mid] < nums[mid-1]    :
                return nums[mid]
            elif nums[mid] > nums[left] :
                left = mid +1
            elif nums[mid] < nums[left] :
                right = mid -1
        if nums[left]<nums[left-1] :
            return nums[left]
solution = Solution()
num = [3,4,5,6,1,2]
a = solution.findMin(num)
print(a)
