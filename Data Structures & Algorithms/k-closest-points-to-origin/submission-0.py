import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kclosest=[]
        for i in range(len(points)):            
            euclidean = (points[i][0]**2 + points[i][1]**2)**0.5
            points[i]=(euclidean,points[i])

        heapq.heapify(points)

        while k > 0:
            distance,coords=heapq.heappop(points)
            kclosest.append(coords)
            k-=1

        return kclosest




                

        
