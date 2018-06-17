class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums

        last = nums[-1]
        start = 0
        end = len(nums)

        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] <= last:
                end = mid
            elif nums[mid] > last:
                start = mid

        return min(nums[start], nums[end])

        return -1