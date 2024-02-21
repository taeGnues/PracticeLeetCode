class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        arr = {}
        ans = 0
        for i in range(len(nums)):
            if not arr :
                arr[nums[i]]=1
            else :
                if nums[i] in arr : continue
                
                if not arr.get(nums[i]-1):
                    if ans < len(arr) : ans = len(arr)
                    arr.clear()
                
                arr[nums[i]]=1

        if ans < len(arr) : ans = len(arr)
        return ans 
        