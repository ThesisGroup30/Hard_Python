from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # Replace variables with their corresponding values
        values = dict(zip(evalvars, evalints))
        def eval(expr):
            if expr.isdigit():
                return [('', int(expr))]
            terms = []
            for e in expr.split('*'):
                if e in values:
                    e = str(values[e])
                if e.isdigit():
                    terms.append(('', int(e)))
                else:
                    terms.append((e, 1))
            return terms
        
        # Parse the expression into a list of terms
        expr = expression.replace('(', '( ').replace(')', ' )')
        stack = [[]]
        for token in expr.split():
            if token.isdigit() or token.isalpha():
                stack[-1].append(eval(token))
            elif token == '(':
                stack.append([])
            elif token == ')':
                term = stack.pop()
                stack[-1].append(term)
            elif token == '+':
                stack[-1].append('+')
            elif token == '-':
                stack[-1].append('-')
            elif token == '*':
                stack[-1][-1] = (stack[-1][-1][0], stack[-1][-1][1]+1)
        
        # Evaluate the expression recursively
        def merge(terms1, terms2, op):
            if op == '+':
                terms = defaultdict(int)
                for var1, coef1 in terms1:
                    terms[var1] += coef1
                for var2, coef2 in terms2:
                    terms[var2] += coef2
                return [(var, coef) for var, coef in terms.items() if coef != 0]
            elif op == '-':
                return merge(terms1, [(var, -coef) for var, coef in terms2], '+')
            elif op == '*':
                terms = []
                for var1, coef1 in terms1:
                    for var2, coef2 in terms2:
                        vars = sorted(var1.split('*') + var2.split('*'))
                        terms.append(('*'.join(vars), coef1*coef2))
                return terms
        
        def evaluate(expr):
            if isinstance(expr, list):
                # Evaluate sub-expressions recursively
                terms = evaluate(expr[0])
                for i in range(1, len(expr), 2):
                    op = expr[i]
                    terms2 = evaluate(expr[i+1])
                    terms = merge(terms, terms2, op)
                return terms
            else:
                # Expression is a single term
                return eval(expr)
        
        # Simplify and format the result
        terms = evaluate(stack[0])
        terms = sorted(terms, key=lambda x: (-len(x[0].split('*')), x[0]))
        return [f"{coef}*{var}" if var else str(coef) for var, coef in terms if coef != 0]
