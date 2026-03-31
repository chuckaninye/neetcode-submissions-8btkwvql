class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        st = []

        for c in s:
            if st and c == ')' and st[-1] == '(':
                st.pop()
                continue
            if st and c == '}' and st[-1] == '{':
                st.pop()
                continue
            if st and c == ']' and st[-1] == '[':
                st.pop()
                continue
            else:
                st.append(c)

            
        
        return True if not st else False
            