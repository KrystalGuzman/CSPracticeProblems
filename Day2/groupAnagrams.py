from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dictionary
        result = {}
        #loop through strs
        for i in strs:
            #puts strings in alpha order
            x = "".join(sorted(i))
            #checks if in result
            if x in result:
                #adds to result
                result[x].append(i)
            else:
                #adds first one to result
                result[x] = [i]
        #returns result
        return list(result.values())