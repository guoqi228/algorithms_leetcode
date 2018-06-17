class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if nums == None or nums == []:
            return -1

        n = len(nums)
        left = 0
        right = n - 1

        while (left + 1) < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1