# Merge Interval with labels
# Input:  []
# Output: []
# Input:  [(0, 3, "A"), (2, 4, "B"), (5, 6, "C")]
# Output: [(0, 2, ["A"]),  (2, 3, ["A", "B"]), (3, 4, ["B"]), (5, 6, ["C"])]
# Input:  [(0, 10, "A"), (2, 9, "B"), (5, 6, "C")]
# Output: [(0, 2, ["A"]),  (2, 5, ["A", "B"]), (5, "6", ["A, B, "C"]), (6, 9, ["B", "A"]), (9, 10, ["A"])]
# Input:  [(0, 3, "A"), (2, 4, "B"), (5, 8, "C"), (5, 7, "A")]
# Output: [(0, 2, ["A"]),  (2, 3, ["A", "B"]), (3, 4, ["B"]), (5, 7, ["C", "A"]), (7, 8, ["C"])]
# Input:  [(0, 3, "A"), (2, 4, "B"), (5, 7, "C"), (5, 7, "A")]
# Output: [(0, 2, ["A"]),  (2, 3, ["A", "B"]), (3, 4, ["B"]), (5, 7, ["C", "A"])]

from enum import Enum
from typing import List, Tuple

class Event(Enum):
    Start = 1
    End = 2

class Solution:
    def mergeIntervals(self, intervals: List[Tuple]) -> List[Tuple]:
        
        if not intervals:
            return []

        events = []
        for interval in intervals:
            if interval[0] > interval[1]:
                raise ValueError("Start Time cannot be greater than end time")
            events.append((interval[0], Event.Start, interval[2]))
            events.append((interval[1], Event.End, interval[2]))

        events.sort(key=lambda x: x[0])
        current = set()
        start, end = None, None
        size = 0
        res = []

        for event in events:
            if event[1] == Event.Start:

                if start is None:
                    start = event[0]       
                    size += 1
                    current.add(event[2])    
                    continue
                
                if end is None:
                    end = event[0]
                    
                if start != event[0]:
                    res.append((start, event[0], list(current)))
                size += 1
                current.add(event[2])
                start, end = end, event[0]

            else:
                if end != event[0]:
                    res.append((start, event[0], list(current)))
                current.remove(event[2])
                size -= 1
                if size == 0:
                    start, end = None, None
                else:
                    start, end = event[0], event[0]
                
        return res

s = Solution()
print(s.mergeIntervals([]))
print(s.mergeIntervals([(0, 3, "A"), (2, 4, "B"), (5, 6, "C")]))
print(s.mergeIntervals([(0, 10, "A"), (2, 9, "B"), (5, 6, "C")]))
print(s.mergeIntervals([(0, 3, "A"), (2, 4, "B"), (5, 8, "C"), (5, 7, "A")]))
print(s.mergeIntervals([(0, 3, "A"), (2, 4, "B"), (5, 7, "C"), (5, 7, "A")]))
