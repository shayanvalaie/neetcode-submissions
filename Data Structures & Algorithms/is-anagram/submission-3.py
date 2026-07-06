class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # time: o(n)

        # space: o(n)

        if len(s) != len(t):
            return False

        sCount, tCount= {}, {}


        for c in s:
            sCount[c] = 1 + sCount.get(c, 0)

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)


        print(sCount, tCount)
        for char, count in sCount.items():
            if char not in tCount or sCount[char] != tCount[char]:
                return False
        return True

        
        
