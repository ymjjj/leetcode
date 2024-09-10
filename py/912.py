from typing import List

class Solution:
    def merge(self,NumsLeft:List[int],NumsRight:List[int]) -> List[int]:
        nums=[]
        left_p,right_p=0,0
        while left_p<len(NumsLeft) and right_p<len(NumsRight):
#这里要用elif，不能用3个if，否则会出现数组越界问题，例子：[5,1,1,2,0,0]
            if NumsLeft[left_p]<NumsRight[right_p]:
                nums.append(NumsLeft[left_p])
                left_p+=1
            elif NumsLeft[left_p]>NumsRight[right_p]:
                nums.append(NumsRight[right_p])
                right_p+=1
            elif NumsLeft[left_p]==NumsRight[right_p]:  #记得加相等时的判断，例子：[5,1,1,2,0,0]
                nums.append(NumsLeft[left_p])
                left_p+=1
        while left_p<len(NumsLeft):
            nums.append(NumsLeft[left_p])
            left_p+=1
        while right_p<len(NumsRight):
            nums.append(NumsRight[right_p])
            right_p+=1
        return nums
    def mergeSort(self, nums: [int]) -> [int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        NumsLeft=self.mergeSort(nums[0:mid])
        NumsRight=self.mergeSort(nums[mid:])
        return self.merge(NumsLeft,NumsRight)
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
solution=Solution()
a=[5,1,1,2,0,0]
nums=solution.sortArray(a)
print(nums)