from typing import List
#自己的做法，效率低#
class MySolution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums=[]
        nums1_p,nums2_p=0,0
        while nums2_p<n and nums1_p<m:
            if nums1[nums1_p]<nums2[nums2_p]:
                nums.append(nums1[nums1_p])
                nums1_p+=1
            elif nums1[nums1_p]>nums2[nums2_p]:
                nums.append(nums2[nums2_p])
                nums2_p+=1
            elif nums1[nums1_p]==nums2[nums2_p]:
                nums.append(nums1[nums1_p])
                nums1_p+=1
        while nums2_p<n :
            nums.append(nums2[nums2_p])
            nums2_p+=1
        while nums1_p<m:
            nums.append(nums1[nums1_p])
            nums1_p+=1
        nums1[:]=nums[:]

#leetcode上的题解，链接：https://leetcode.cn/problems/merge-sorted-array/solutions/2850006/ni-xiang-fu-zhi-ppt-dong-hua-fei-chang-y-kpq3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tail = len(nums1) - 1
        i1 = m - 1
        i2 = n - 1

        # 个人经常用 while true，然后在循环内部列出所有情况
        while True:
            # 都左移到头，退出
            if i1 == -1 and i2 == -1:
                break
            # 一方左移到头，选取另一方赋值，然后左移
            elif i1 == -1:
                nums1[tail] = nums2[i2]
                i2 -= 1
            elif i2 == -1:
                nums1[tail] = nums1[i1] # 也可以省去，直接 i1 -= 1;
                i1 -= 1
            # 选取大的元素赋值，然后左移
            elif nums1[i1] > nums2[i2]:
                nums1[tail] = nums1[i1]
                i1 -= 1
            else:
                nums1[tail] = nums2[i2]
                i2 -= 1
            tail -= 1

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

solution=Solution()
solution.merge(nums1,m,nums2,n)
print(nums1)       