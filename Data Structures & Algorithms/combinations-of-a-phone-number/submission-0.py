class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitsMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
            else:
                for c in digitsMap[digits[i]]:
                    path.append(c)
                    backtrack(i + 1, path)
                    path.pop()
            
        res = []
        if digits:
            backtrack(0, [])
            return res
        else:
            return []