from typing import List

#桶排序法
class Solution:
    
    def bucketsort(self,nums:List[int],indexDiff: int,valueDiff : int ) ->bool :
            #桶大小
            bucket_size = valueDiff+1
            #桶数
            nums_min, nums_max = min(nums), max(nums)
            bucketcount = (nums_max-nums_min)//(bucket_size) + 1
            #建桶
            buckets = [[] for _ in range(bucketcount)]
            #分桶 这么分的原因见：https://leetcode.cn/problems/contains-duplicate-iii/和 
            #  https://algo.itcharge.cn/Solutions/0200-0299/contains-duplicate-iii/#%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF
            for i in range(len(nums)) :
                #确定该元素在哪个桶
                bucket_num = (nums[i]-nums_min)//bucket_size
                if len(buckets[bucket_num]) == 0 :
                    #假如该桶是个空桶,将该元素放入桶
                    buckets[bucket_num].append(nums[i])
                    #判断它前面的桶内的元素与该元素的差是否符合要求
                    #外层if作用为判断该桶前面有没有桶，以及前面的桶是否为空
                    if (bucket_num-1)>=0 and (len(buckets[bucket_num-1])>0) :
                        #判断两元素的差是否小于等于valueDiff
                        if abs(buckets[bucket_num][0]-buckets[bucket_num-1][0]) <= valueDiff:
                            return True
                    #判断它后面的桶内的元素与该元素的差是否符合要求
                    #外层if作用为判断该桶后面有没有桶，以及后面的桶是否为空
                    if (bucket_num+1) < bucketcount and (len(buckets[bucket_num+1])>0) :
                        #判断两元素的差是否小于等于valueDiff
                        if abs(buckets[bucket_num][0]-buckets[bucket_num+1][0]) <= valueDiff:
                            return True
                    #当 i < indesDiff 时，桶中所有元素之间的角标差都小于indexDiff
                    #当 i >= indexDiff 时，将nums[i-k]从其所在的桶中删掉，这样可以保证，当i=i+1时，所有桶中的元素都符合indexDiff条件
                    #由于桶中只有一个元素，直接用pop函数
                    if i>= indexDiff :
                        buckets[(nums[i-indexDiff]-nums_min)//bucket_size].pop()
                else :
                    return True
            return False
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        return self.bucketsort(nums,indexDiff,valueDiff)
solution = Solution()
nums=[3,6,0,4]
a=solution.containsNearbyAlmostDuplicate(nums,2,2)
print(a)