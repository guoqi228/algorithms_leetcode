class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here

        if nums is None or len(nums) == 0:
            return None

        n = len(nums)

        if n == 1:
            return nums[0]

        start = 0
        end = n - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid

        return max(nums[start], nums[end])