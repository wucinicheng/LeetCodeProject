class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = 0
        count = 0
        length = len(nums)
        remove_num = 0
        for i in range(length):
            index = i - remove_num
            num = nums[index]
            if num == key:
                count = count + 1
            else:
                key = num
                count = 1

            if count > 2:
                nums.pop(index)
                count = count - 1
                remove_num = remove_num + 1
        return len(nums), nums

s = Solution()
nums = [1,1,1,2,2,3]
n, nums = s.removeDuplicates(nums)
print(n)
print(nums)

# 总结：难点在于在查找过程中需要删除可能会使得数组长度发生变化