#time complexity O(n) - go through the array once, and each lookup in the set takes O(1) on avg.
#space complexity O(n) - in the worst case, we might store all numbers in the set.

# if choose a list, each lookup could take O(n), and the whole solution would be O(n^2).

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num) 
            #不需要写else, 因为在if中已经return true，
            #所以如果程序继续往下执行，就说明当前数字不存在在seen里面

        return False