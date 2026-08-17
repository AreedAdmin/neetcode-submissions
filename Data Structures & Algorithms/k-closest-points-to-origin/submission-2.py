import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):            
            euclidean = points[i][0]**2 + points[i][1]**2
            points[i]=(euclidean,points[i])

        heapq.heapify(points)

        return [heapq.heappop(points)[1] for i in range(k)]




                

        
