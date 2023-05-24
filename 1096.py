class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(index: int) -> Set[str]:
            unions = []
            concat = {''}

            while index < len(expression):
                if expression[index] == '{':
                    j = index + 1
                    count = 1

                    while count > 0:
                        if expression[j] == '{':
                            count += 1
                        elif expression[j] == '}':
                            count -= 1
                        j += 1

                    sub = parse(index + 1)
                    unions.append(sub)
                    index = j
                elif expression[index] == ',' or expression[index] == '}':
                    unions.append(concat)
                    concat = {''}
                    index += 1
                else:
                    char = expression[index]
                    new_concat = set()

                    for word in concat:
                        new_concat.add(word + char)

                    concat = new_concat
                    index += 1

            for sub in unions:
                concat = {word + sub_word for word in concat for sub_word in sub}

            return concat

        return sorted(parse(0))
