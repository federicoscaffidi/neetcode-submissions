class Solution:
    def climbStairs(self, n: int) -> int:

        climb_costs = [0 for _ in range(n+1)]

        def helper(n: int):
            if n == 2:
                return 2
            elif n == 1:
                return 1
            if not climb_costs[n-1]:
                climb_costs[n-1] = helper(n-1)
            if not climb_costs[n-2]:
                climb_costs[n-2] = helper(n-2)
            return climb_costs[n-1] + climb_costs[n-2]

        return helper(n)