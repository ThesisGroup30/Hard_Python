import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Determine the number of tests each pig can perform
        tests_per_pig = math.floor(minutesToTest / minutesToDie) + 1
        
        # Determine the number of pigs required to test all the buckets
        num_pigs = math.ceil(math.log(buckets) / math.log(tests_per_pig))
        
        return num_pigs
