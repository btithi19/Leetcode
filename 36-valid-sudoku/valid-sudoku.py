class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(9):
            seen = []

            for j in range(9):
                number = board[i][j]

                if number != ".":
                    if number in seen:
                        return False
                    seen.append(number)

       
        for j in range(9):
            seen = []

            for i in range(9):
                number = board[i][j]

                if number != ".":
                    if number in seen:
                        return False
                    seen.append(number)

        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        number = board[i][j]

                        if number != ".":
                            if number in seen:
                                return False
                            seen.append(number)

        return True