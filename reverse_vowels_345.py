class Solution:
    def reverseVowels(self, s: str) -> str:
        nums = [i for i in s]
        start, end = 0, len(nums) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while start < end:
            if nums[start] in vowels and nums[end] in vowels:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            elif nums[start] in vowels:
                end -= 1
            elif nums[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        return ''.join(nums)
