class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        DataFrame = {}
        for i in range(len(nums)):
            if not nums[i] in DataFrame.keys():
                DataFrame[target - nums[i]] = i
            else:
                return [DataFrame[nums[i]], i]