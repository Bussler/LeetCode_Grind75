from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re 



class Insert_Interval_Solver(Solver):

    def solve(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        newList=[]
        new_start=-1
        new_end=-1
        
        interval_start = newInterval[0]
        interval_end = newInterval[1]
        
        # TODO: check for first/ last element
        for i in range(len(intervals)):
            cur_i = intervals[i]
            
            # M: find start
            if new_start == -1 and interval_start <= cur_i[0]:
                new_start = min(interval_start, cur_i[0])
            
            if new_start == -1 and interval_start >= cur_i[0] and interval_start <=cur_i[1]:
                new_start = min(interval_start, cur_i[0])
            
            # M: find end
            # M: Case: End is not in cur interval
            if new_start >= 0 and interval_end >= cur_i[1]:
                # M: End is before next interval
                if i+1 < len(intervals) and interval_end < intervals[i+1][0]:
                    new_end = interval_end
            
            # M: Case: End is in cur interval
            if new_start >= 0 and interval_end >= cur_i[0] and interval_end <= cur_i[1]:
                new_end = max(interval_end, cur_i[1])
                
            # M: Case: End is before cur interval
            if new_start >= 0 and interval_end < cur_i[0]:
                newList.append([new_start, interval_end])
                new_start = -2
                new_end = -2
                
            # M: Default case: copy existing interval
            if new_start <= -1 and new_end <= -1:
                newList.append(cur_i)
                
            if new_start >= 0 and new_end >= 0:
                newList.append([new_start, new_end])
                new_start = -2
                new_end = -2
                
        if new_start >= 0 and new_end <= -1:
            newList.append([new_start, interval_end])
            
        if new_start == -1 and new_end == -1:
            newList.append([interval_start, interval_end])

        return newList

    def test_solve(self):
        #intervals = [[1,3],[6,9]]
        #newInterval = [2,5]
        
        intervals = [[1,5]]
        newInterval = [0,0]
        
        #intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        #newInterval = [4,8]
    
        new_Intervals = self.solve(intervals, newInterval)
        print("Merged Intervals: ", new_Intervals)