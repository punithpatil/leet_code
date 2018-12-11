# https://leetcode.com/problems/combination-sum/

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        # Caculating lenght before hand caused 4ms speed up
        candidates_length = len(candidates)
        def backtrack(start_index, sum_so_far, combinations):
            nonlocal candidates, target, output
            if sum_so_far > target:
                return
            if sum_so_far == target:
                output.append(combinations)
            for i in range(start_index, candidates_length):
                backtrack(i,
                          sum_so_far + candidates[i],
                          combinations + [candidates[i]]
                         )
        
        backtrack(0, 0, [])
        
        return output