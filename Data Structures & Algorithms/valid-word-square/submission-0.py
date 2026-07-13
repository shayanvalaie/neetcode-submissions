class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        

        ROWS, COLS = len(words), len(words[0])
        rowsToString, colsToString = collections.defaultdict(str), collections.defaultdict(str)


        for r in range(ROWS):
            for c in range(len(words[r])):
                rowsToString[r] += words[r][c]
                colsToString[c] += words[r][c]
        print(rowsToString)
        print(colsToString)


        for key, string in rowsToString.items():
            if key in colsToString and rowsToString[key] != colsToString[key]:
                return False
        return True