class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    Definition of ArrayReader:
    class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        start, end = 0, index

        while start + 1 < end:
            mid = int((start + end) / 2)
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            elif reader.get(mid) > target:
                end = mid

        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end

        return -1