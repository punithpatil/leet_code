# https://leetcode.com/problems/count-primes/

# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # cell = False, not prime
        # cell = True, prime
        sieve = [True]*(n+1)
        primes_count = 0
        
        for i in range(2,n):
            if sieve[i]:
                primes_count += 1
                prime = i
                factor = 2*prime
                step = 1
                while factor <= n:
                    sieve[factor] = False
                    factor += prime
                    
        return primes_count
                    
                
