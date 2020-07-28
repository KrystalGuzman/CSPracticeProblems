class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapping = {}
        for i in range(len(nums)):
            curr = nums[i]
            compliment = target - curr
            if compliment in index_mapping:
                return [index_mapping[compliment], i]
            else:
                index_mapping[curr] = i