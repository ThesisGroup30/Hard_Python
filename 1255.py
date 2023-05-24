from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Create a dictionary to store the score for each letter
        letter_score = {chr(i+97): score[i] for i in range(26)}

        # Create a counter for the letters available
        letter_count = Counter(letters)

        # Recursive function to find the maximum score
        def find_max_score(word_index, letter_count):
            # If we have reached the end of the words list, return 0
            if word_index == len(words):
                return 0
            
            # Calculate the score if we include the current word
            word_score = sum([letter_score[c] for c in words[word_index] if letter_count[c] > 0])
            new_letter_count = letter_count.copy()
            new_letter_count.subtract(Counter(words[word_index]))
            include_score = word_score + find_max_score(word_index+1, new_letter_count)
            
            # Calculate the score if we exclude the current word
            exclude_score = find_max_score(word_index+1, letter_count)
            
            # Return the maximum score
            return max(include_score, exclude_score)
        
        # Call the recursive function to find the maximum score
        return find_max_score(0, letter_count)
