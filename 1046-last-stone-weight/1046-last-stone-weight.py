class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            x = sorted(stones)[-1]
            y = sorted(stones)[-2]
            if(x == y):
                stones.remove(x)
                stones.remove(y)
            else:
                stones.append(abs(x-y))
                stones.remove(x)
                stones.remove(y)
        if(len(stones) == 0):
            return 0
        else:
            return stones[0]