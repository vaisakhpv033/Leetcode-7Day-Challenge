class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        for idx, val in enumerate(nums):
            if val != 0:
                nums[zero_ptr], nums[idx] = nums[idx], nums[zero_ptr]
                zero_ptr += 1
        
