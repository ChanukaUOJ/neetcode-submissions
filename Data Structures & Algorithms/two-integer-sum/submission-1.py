class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 

        store = {}
        
        for i,x in enumerate(nums):
            rem = target - nums[i]
            if rem in store.keys():
                return [store[rem],i]
            else:
                store[nums[i]] = i


