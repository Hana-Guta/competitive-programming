class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = list()
        for i in intervals:
            if i[0] <=intervals[0][1]:
                intervals[0][1] = max(i[1],intervals[0][1])
            else:
                arr.append(intervals[0])
                intervals[0] = i
        arr.append(intervals[0])
        return arr
