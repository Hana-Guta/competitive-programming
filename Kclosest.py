class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        answer=[]
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            distance.append((math.sqrt(xi**2 +yi**2),points[i]))
        distance.sort()
        for j in range(k):
            answer.append(distance[j][1])
        return answer
