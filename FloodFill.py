from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que = deque()
        origColor = image[sr][sc]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        que.append((sr, sc))
        visited[sr][sc] = True
        image[sr][sc] = newColor

        while que:
            r, c = que.pop()
            for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newr = r + adj[0]
                newc = c + adj[1]
                if (0 <= newr < len(image) and 0 <= newc < len(image[0])) and (visited[newr][newc] == False) and (
                        image[newr][newc] == origColor):
                    visited[newr][newc] = True
                    image[newr][newc] = newColor
                    que.append((newr, newc))
        return image
