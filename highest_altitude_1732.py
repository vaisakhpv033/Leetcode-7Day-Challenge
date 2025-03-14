class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum, total = 0, 0
        for i in gain:
            total += i
            if total > maximum:
                maximum = total
        return maximum
