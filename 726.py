class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        freq = {}
        curr_element = ''
        curr_count = 0

        def update_freq(element, count):
            if element in freq:
                freq[element] += count
            else:
                freq[element] = count

        for char in formula:
            if char.isupper():
                if curr_element:
                    update_freq(curr_element, curr_count)
                curr_element = char
                curr_count = 0
            elif char.islower():
                curr_element += char
            elif char.isdigit():
                curr_count = curr_count * 10 + int(char)
            elif char == '(':
                stack.append((curr_count, freq))
                curr_count = 0
                freq = {}
            elif char == ')':
                if curr_element:
                    update_freq(curr_element, curr_count)
                count, prev_freq = stack.pop()
                for element, element_count in freq.items():
                    if element in prev_freq:
                        prev_freq[element] += element_count * count
                    else:
                        prev_freq[element] = element_count * count
                curr_count = 0
                freq = prev_freq

        if curr_element:
            update_freq(curr_element, curr_count)

        elements = sorted(freq.keys())
        result = ''
        for element in elements:
            count = freq[element]
            result += element
            if count > 1:
                result += str(count)

        return result
