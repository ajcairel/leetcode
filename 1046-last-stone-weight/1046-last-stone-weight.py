class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            x = sorted(stones)[-2]
            y = sorted(stones)[-1]
            if(x == y):
                stones.remove(x)
                stones.remove(y)
            else:
                stones.append(y-x)
                stones.remove(x)
                stones.remove(y)
        if(len(stones) == 0):
            return 0
        else:
            return stones[0]