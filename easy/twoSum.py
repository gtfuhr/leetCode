class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if num_i + num_j == target:
                    return i,j
