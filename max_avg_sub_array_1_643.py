class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = sum(nums[:k])
        total = maximum
        start, end = 1, 1+k
        while end <= len(nums):
            total -= nums[start-1]
            total += nums[end-1]
            if total > maximum:
                maximum = total
            start += 1
            end +=1
        return maximum/k
