from typing import List

#消消乐法

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0 
        times = 0
        for i in range(0,len(nums)) :
            if times == 0 :
                answer = nums[i]
            if answer == nums[i] :
                times+=1
            else :
                times-=1
            if times == 0 :
                answer = nums[i]
        return answer    

mysolution=Solution()
nums=[2,2,1,1,1,2,2]
i=mysolution.majorityElement(nums)
print(i)
