class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cache = {} 
        for i in arr:
            cache[i] = cache.get(i, 0) + 1
        values = set()
        for value in cache.values():
            if value in values:
                return False
            values.add(value)
        return True
