class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointsNumber=len(points)
        minimumTime=0
        if 1==pointsNumber:
            return minimumTime
        for i in range(pointsNumber-1):
            orbit1=points[i][1]-points[i][0]
            orbit2=points[i+1][1]-points[i+1][0]
            orbit3=points[i][1]+points[i][0]
            orbit4=points[i+1][1]+points[i+1][0]
            minimumTime+=min(abs(points[i+1][1]-points[i][1]),abs(points[i+1][0]-points[i][0]))+min(abs(orbit2-orbit1),abs(orbit4-orbit3))
        return minimumTime
    

sln=Solution() 
assert 5==sln.minTimeToVisitAllPoints(points = [[3,2],[-2,2]])
assert 7==sln.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])
assert 0==sln.minTimeToVisitAllPoints(points = [[0,0]])
assert 4==sln.minTimeToVisitAllPoints(points = [[3,2],[-1,0]])
assert 2==sln.minTimeToVisitAllPoints(points = [[-1,0],[-2,2]])
assert 6==sln.minTimeToVisitAllPoints(points = [[3,2],[-1,0],[-2,2]])