from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
            else:
                if temp>max:
                    max=temp
                temp=0
        if temp>max:
            max=temp
        return max
    
solution=Solution()
nums=[1,1,0,1,1,1]
a=solution.findMaxConsecutiveOnes(nums)
print(a)