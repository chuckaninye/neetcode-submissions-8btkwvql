class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        origColor = image[sr][sc]

        if image[sr][sc] == color:
            return image
            
        image[sr][sc] = color
        ROWS, COLS = len(image), len(image[0])
        q = collections.deque()
        q.append((sr, sc))

        

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and image[nr][nc] == origColor:
                    image[nr][nc] = color
                    q.append((nr, nc))
            
        return image