class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        r = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for l in range(i+1,len(nums)-2):
                if l>i+1 and nums[l]==nums[l-1]:
                    continue
                j = l+1
                k = len(nums)-1
                while j<k:
                    s = nums[i]+nums[l]+nums[j]+nums[k]
                    if s == target:
                        r.append([nums[i],nums[l],nums[j],nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j = j+1
                        while j<k and nums[k]==nums[k-1]:
                            k = k-1
                        j = j+1
                        k = k-1
                    elif s<target:
                        j = j+1
                    else:
                        k=k-1
        return r
                    
                    



                