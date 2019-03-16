# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        
        def helper(nums1, nums2):
            x = len(nums1)
            y = len(nums2)

            start = 0
            end = x
            half_len = (x + y + 1)//2
            
            while start <= end:
                partition_x = (start+end)//2
                partition_y = half_len - partition_x

                max_left_x  = -math.inf if partition_x == 0 else nums1[partition_x - 1]
                min_right_x =  math.inf if partition_x == x else nums1[partition_x] 

                max_left_y  = -math.inf if partition_y == 0 else nums2[partition_y - 1]
                min_right_y =  math.inf if partition_y == y else nums2[partition_y]

                if max_left_x <= min_right_y and max_left_y <= min_right_x:
                    if (x+y)%2 == 0:
                        return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2
                    else:
                        return max(max_left_x, max_left_y)
                elif max_left_y > min_right_x:
                    # need to jump right
                    start = partition_x + 1
                else:
                    # need to jump left
                    end = partition_x - 1
                    
        if len(nums1) > len(nums2):
            return helper(nums2, nums1)
        else:
            return helper(nums1, nums2)