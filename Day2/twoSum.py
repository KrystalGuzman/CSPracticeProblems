class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dict
        index_mapping = {}
        #loop through list
        for i in range(len(nums)):
            #set current
            curr = nums[i]
            #set compliment
            compliment = target - curr
            #checks if in index mapping
            if compliment in index_mapping:
                return [index_mapping[compliment], i]
            #adds to index mapping
            else:
                index_mapping[curr] = i