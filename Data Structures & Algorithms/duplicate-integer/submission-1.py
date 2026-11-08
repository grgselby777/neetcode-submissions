class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #objective: if any value appears more than once in the set, spit false, if it all appears once, spit true 
        check = set() #set only accepts one of a value 
        for n in nums:
            if n in check:
                return True 
            check.add(n)
        return False 

        