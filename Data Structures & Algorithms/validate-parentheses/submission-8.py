class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            if stack and c == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and c == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)

        return True if not stack else False