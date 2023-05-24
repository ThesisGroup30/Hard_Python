class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Initialize an empty hash table.
        d = {}
        
        # Fill in the hash table with the reverse of each word and its index.
        for i, w in enumerate(words):
            d[w[::-1]] = i
        
        # Initialize an empty list to store the palindrome pairs.
        res = []
        
        # Loop through each word and check for palindrome pairs.
        for i, w in enumerate(words):
            n = len(w)
            
            # Check for a palindrome pair with an empty string.
            if "" in d and w != "" and w == w[::-1]:
                res.append([i, d[""]])
                res.append([d[""], i])
            
            # Check for a palindrome pair where the two words are the same, but their indices are different.
            if w[::-1] in d and d[w[::-1]] != i:
                res.append([i, d[w[::-1]]])
            
            # Check for palindrome pairs where the first word is shorter than the second word.
            for j in range(1, n+1):
                prefix = w[:j]
                suffix = w[j:]
                if prefix == prefix[::-1] and suffix[::-1] in d:
                    res.append([d[suffix[::-1]], i])
                if suffix == suffix[::-1] and prefix[::-1] in d:
                    res.append([i, d[prefix[::-1]]])
            
            # Check for palindrome pairs where the first word is longer than the second word.
            for j in range(n-1, 0, -1):
                prefix = w[:j]
                suffix = w[j:]
                if prefix == prefix[::-1] and suffix[::-1] in d:
                    res.append([i, d[suffix[::-1]]])
                if suffix == suffix[::-1] and prefix[::-1] in d:
                    res.append([d[prefix[::-1]], i])
        
        return res
