class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1
        
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif ch == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ch == ')':
                result += sign * operand
                operand = 0
                result *= stack.pop()
                result += stack.pop()
                
        if operand != 0:
            result += sign * operand
            
        return result
