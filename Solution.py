class Solution:
    def countStableSubsequences(self, nums):
        MOD = 10 ** 9 + 7
        dp = [[0, 0] for _ in range(3)]  # dp[count][parity]
        total = 0

        for num in nums:
            parity = num % 2
            new_dp = [[0, 0] for _ in range(3)]

            # Start a new subsequence
            new_dp[1][parity] = 1

            # Extend existing subsequences
            for count in [1, 2]:
                for p in [0, 1]:
                    if p == parity:
                        if count < 2:
                            new_dp[count + 1][parity] = (new_dp[count + 1][parity] + dp[count][p]) % MOD
                    else:
                        new_dp[1][parity] = (new_dp[1][parity] + dp[count][p]) % MOD

            # Update dp and total
            for count in [1, 2]:
                for p in [0, 1]:
                    dp[count][p] = (dp[count][p] + new_dp[count][p]) % MOD
                    total = (total + new_dp[count][p]) % MOD

        return total
