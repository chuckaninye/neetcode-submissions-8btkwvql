class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        stack = []

        for c in s:
            if stack and c == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and c == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0