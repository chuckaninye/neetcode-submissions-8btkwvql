class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        ROW = len(image)
        COL = len(image[0])


        oldColor = image[sr][sc]
        if oldColor == color:
            return image
            
        image[sr][sc] = color
        q = collections.deque([(sr, sc)])

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < ROW and nc >= 0 and nc < COL and image[nr][nc] == oldColor:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image