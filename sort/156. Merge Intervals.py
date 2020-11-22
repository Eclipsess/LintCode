"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here
        if not intervals:
            return intervals
        sort_intervals = sorted(intervals, key=lambda x: x.start)

        l, h = 0, 1
        while h < len(sort_intervals):
            if sort_intervals[l].end < sort_intervals[h].start:
                l += 1
                sort_intervals[l] = sort_intervals[h]
                h += 1
            else:
                sort_intervals[l].end = max(sort_intervals[l].end, sort_intervals[h].end)
                h += 1

        return sort_intervals[:l + 1]