'''
Q: 주어진 스도쿠배열이 올바른지 확인
A:
    가로, 세로, 3*3 구역별로 "."을 제외한 나머지 숫자 중 중복이 있는지 확인
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        for i in range(9):
            check = []
            for j in range(9):
                if board[i][j] != ".":
                    check.append(board[i][j])
            if len(check) != len(set(check)):
                return False
        
        for i in range(9):
            check = []
            for j in range(9):
                if board[j][i] != ".":
                    check.append(board[j][i])
            if len(check) != len(set(check)):
                return False
            
        for n in range(3):
            for m in range(3):
                check = []
                for i in range(3):
                    for j in range(3):
                        if board[3*n+i][3*m+j] != ".":
                            check.append(board[3*n+i][3*m+j])
                if len(check) != len(set(check)):
                    return False
        return True