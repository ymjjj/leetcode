from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=k%len(nums)
        arr = [0 for _ in range(len(nums))]
        for j in  range(len(nums)) :
            arr[j]=nums[j-i]
        for m in range(len(nums)) :
            nums[m]=arr[m]
solution = Solution()
nums=[1,2,3,4,5,6,7]
k=3
solution.rotate(nums, k)
print(nums)
