"""
My solution to the 1106 LeetCode's problem, a challenge from 20th October 2024.

Runtime: 17 ms
Allocated memory: 16.76 MB
Complexity: O(n)
Difficulty: Hard

https://leetcode.com/problems/parsing-a-boolean-expression/description/
"""

class Solution:
    def __init__(self):
        self.expressions = {'&': self._and, '|': self._or, '!': self._not}

    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression == 't'
        return self.expressions[expression[0]](expression)
        
    def _and(self, expression: str) -> bool:
        sub_exprs = self.split_expression(expression)
        for sub_expr in sub_exprs:
            if not self.parseBoolExpr(sub_expr):
                return False
        return True # all
        
    def _or(self, expression: str) -> bool:
        sub_exprs = self.split_expression(expression)
        for sub_expr in sub_exprs:
            if self.parseBoolExpr(sub_expr):
                return True # any
        return False
        
    def _not(self, expression: str) -> bool:
        return not self.parseBoolExpr(expression[2:-1])

    def split_expression(self, expression: str) -> list:
        sub_exprs = expression[2:-1]
        expressions = ['']
        expected_closed = 0
        sub_expr_i = 0
        for i in sub_exprs:
            if expected_closed == 0 and i == ',':
                sub_expr_i += 1
                expressions.append('')
                continue

            expressions[sub_expr_i] += i
    
            if i == '(':
                expected_closed += 1
            elif i == ')':
                expected_closed -= 1
        return expressions
