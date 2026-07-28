class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        origColor = image[sr][sc]
        image[sr][sc] = color
        q = deque()
        q.append((sr, sc))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= 0 and nr < len(image) and nc >=0 and nc < len(image[0]) and image[nr][nc] == origColor:
                    image[nr][nc] = color
                    q.append((nr, nc))
                
        return image