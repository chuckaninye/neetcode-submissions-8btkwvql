class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1, str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            else:
                return False
        
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res