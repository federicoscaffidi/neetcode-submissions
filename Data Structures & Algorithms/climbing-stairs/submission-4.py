class Solution:
    def climbStairs(self, n: int) -> int:

        climb_cost = [0 for _ in range(n+1)]
        if n>0:
            climb_cost[1] = 1
        if n>1:
            climb_cost[2] = 2

        for step in range(3, n+1):
            climb_cost[step] = climb_cost[step-1] + climb_cost[step-2]

        return climb_cost[n]