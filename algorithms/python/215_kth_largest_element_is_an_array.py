# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        import math
        
        # Convert to Hth smallest element
        # H = len(nums) - k
        h = len(nums) - k 
        
        # https://en.wikipedia.org/wiki/Quickselect
        
        def partition(nums, left, right, pivot_index):
            pivot_value = nums[pivot_index]
            # Put pivot at the end of the array
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            store_index = left
            # Move elements until pivot sits in the sorted position
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # Last swap to bring pivot into sorted order
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index
        
        def select(nums, left, right, h):
            if left == right:
                return nums[left]
            #88ms run time
            pivot_index = left + math.floor(int(random.random()*100000000) % 
                                           (right - left + 1))
            #1288 ms runtime
            #pivot_index = right
            pivot_index = partition(nums, left, right, pivot_index)
            
            if h == pivot_index:
                return nums[h]
            elif h < pivot_index:
                return select(nums, left, pivot_index -1, h)
            else:
                return select(nums, pivot_index + 1, right, h)

        #84ms runtime
        random.shuffle(nums)
        return select(nums, 0, len(nums) - 1, h)
            