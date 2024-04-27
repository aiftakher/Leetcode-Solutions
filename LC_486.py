# LC 486

'''
dynamic zero sum game (min max) 
'''
class Solution:
    def predictTheWinner(self, nums):
        def recursion(i, j, turn):
            if i > j:
                return 0
            if turn == 0:  # Player A's turn
                pick_i = nums[i] + recursion(i+1, j, 1)  # Score if A picks nums[i]
                pick_j = nums[j] + recursion(i, j-1, 1)  # Score if A picks nums[j]
                return max(pick_i, pick_j)  # Maximize A's score
            else:  # Player B's turn
                pick_i = recursion(i+1, j, 0)  # Score if B picks nums[i]
                pick_j = recursion(i, j-1, 0)  # Score if B picks nums[j]
                return min(pick_i, pick_j)  # Minimize A's score, maximize B's score

        total = sum(nums)
        scoreA = recursion(0, len(nums)-1, 0)
        return scoreA >= (total - scoreA)

# Example usage:
sol = Solution()
nums = [1, 5, 2]
print(sol.predictTheWinner(nums))
