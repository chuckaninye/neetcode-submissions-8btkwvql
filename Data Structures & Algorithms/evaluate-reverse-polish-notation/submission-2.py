class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                two = stack.pop()
                one = stack.pop()
                stack.append(one - two)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                two = stack.pop()
                one = stack.pop()
                stack.append(int(one / two))
            else:
                stack.append(int(c))

        return stack[-1]

        5
        13
        4