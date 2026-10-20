class Solution:
    def climbStairs(self, n: int) -> int:

        climb_cost = [0, 1, 2, 0]
        if n==1:
            return 1
        if n==2:
            return 2

        for step in range(3, n+1):
            climb_cost[3] = climb_cost[2] + climb_cost[1]
            climb_cost[1] = climb_cost[2]
            climb_cost[2] = climb_cost[3]

        return climb_cost[3]