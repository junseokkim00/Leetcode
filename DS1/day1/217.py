class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        
        return False