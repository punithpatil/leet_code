# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates_length = len(candidates)
        def backtrack(start_index, sum_so_far, combinations):
            nonlocal target, candidates, output
            if sum_so_far > target:
                return
            if sum_so_far == target:
                output.append(combinations)
            
            for i in range(start_index, candidates_length):
                # Skip duplicates
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1,
                          sum_so_far + candidates[i],
                          combinations + [candidates[i]]
                         )
            
        candidates.sort()    
        backtrack(0, 0, [])
        return output
                