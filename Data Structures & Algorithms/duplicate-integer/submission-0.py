class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            hash_set.add(i)
        if len(nums) != len(hash_set):
            return True
        else:
            return False