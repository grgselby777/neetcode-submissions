class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_i = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                    sum_i.append(i)
                    sum_i.append(j)
        return {sum_i}
        