class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    a.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j]==nums[j+1]:
                        j = j+1
                    while j<k and nums[k]==nums[k-1]:
                        k = k-1
                    j=j+1
                    k=k-1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j= j+1
                else:
                    k = k-1
        return a