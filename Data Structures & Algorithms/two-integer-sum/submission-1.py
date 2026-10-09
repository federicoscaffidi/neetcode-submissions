class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        for i in range(len(nums)):
            if mem.get(target-nums[i]) not in (None, i):
                res = [mem.get(target-nums[i]), i]
                return res
            mem[nums[i]] = i
            