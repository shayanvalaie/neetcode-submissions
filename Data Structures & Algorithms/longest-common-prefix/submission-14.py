class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ''
    
        firstWord = strs[0]

        for i in range(len(strs[0])):
            c = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return firstWord[:i]
        return firstWord

                

   
