from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num = 0
        summary = arr[0]
        left = 0
        right = 0
        if len(arr) == 1 :
            if arr[0] >= threshold :
                return 1
            else :
                return 0
        while right < len(arr) :
            if (right - left + 1) >= k:
                average = summary/k
                if average >= threshold :
                    num += 1
                summary -= arr[left]
                left += 1
            right += 1
            if right < len(arr) :
                summary += arr[right]
        return num
solution = Solution()
arr = [11,13,17,23,29,31,7,5,2,3]
a = solution.numOfSubarrays(arr,3,5)
print(a)