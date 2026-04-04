class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == "}" and st and st[-1] == "{":
                st.pop()
            elif c == "]" and st and st[-1] == "[":
                st.pop()
            elif c == ")" and st and st[-1] == "(":
                st.pop()
            else:
                st.append(c)

        return True if not st else False
