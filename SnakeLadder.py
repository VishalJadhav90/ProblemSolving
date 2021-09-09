from collections import deque

class Solution:
    def reachDestination(self, pos, ladders, snakes, dicerolls, sol, visited):
        que = deque()
        que.append((pos, 0))
        visited[pos] = True
        while que:
            pos, rolls = que.popleft()
            #print("pos", pos)
            if pos == 100:
                #print("dicerolls", rolls)
                sol['min_rolls'] = min(sol['min_rolls'], rolls)
            elif pos in ladders:
                newpos = ladders[pos]
                visited[newpos] = True
                que.append((newpos, rolls))
            elif pos in snakes:
                newpos = snakes[pos]
                visited[newpos] = True
                que.append((newpos, rolls))
            else:
                for diceroll in range(6, 0, -1):
                    newpos = pos + diceroll
                    if newpos <= 100 and visited[newpos] == False:
                        visited[newpos] = True
                        que.append((newpos, rolls+1))

    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def snakeLadder(self, A, B):
        ladders = {}
        for entry in A:
            ladders[entry[0]] = entry[1]

        snakes = {}
        for entry in B:
            snakes[entry[0]] = entry[1]

        visited = [False for _ in range(0, 102)]
        sol = {'min_rolls': 100}
        self.reachDestination(1, ladders, snakes, 0, sol, visited)
        print("sol", sol)
        return -1 if sol['min_rolls'] >= 100 else sol['min_rolls']


sol = Solution()
ladders = [[3, 90]]
snakes = [[99, 10], [97, 20], [98, 30], [96, 40], [95, 40], [94, 60]]
ladders = [
  [5, 66],
  [9, 88]
]
snakes = [
  [67, 8]
]

sol.snakeLadder(ladders, snakes)