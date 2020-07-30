class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            #find location of target with for loop
            for i in range (0, len(nums)):
                if target == nums[i]:
                    return i
        return -1