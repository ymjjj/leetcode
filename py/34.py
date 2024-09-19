from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        result = []
        while left < right :
            mid = left + (right - left)//2
            if nums[mid] < target :
                left = mid + 1                
            else :
                right = mid
        if nums[left] == target :
            result.append(right)
        else :
            return [-1,-1]
        right = len(nums)-1
        
        while left < right :
            mid = left + (right - left + 1) // 2
            if nums[mid] > target :
                right = mid - 1                
            else :
                left = mid
        if nums[left] == target :
            result.append(left)
        else :
            return [-1,-1]
        return result
        
solution=Solution()
nums = [5,7,7,8,8,10]
a=solution.searchRange(nums,6)    
print(a)  

