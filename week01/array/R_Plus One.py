'''
Q: 배열로 표현된 수의 +1된 값을 배열로 반환하기
A:
    1. 일의 자리 수부터 큰 자리수까지 역으로 확인
    2. 자릿수가 0~8이면 해당값을 +1하고 종료
    3. 자릿수가 9이면 더 큰 자릿수 확인
    4. 2-3 과정 반복(iteration), 만약 가장 큰 자릿수도 9이면 맨 앞에 1 추가
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = len(digits) - 1
        self.iterCheck(digits, k)
        return digits
    
    def iterCheck(self, digits: List[int], k: Integer):
        if digits[k] < 9:
            digits[k] += 1
        else:
            digits[k] = 0
            if k-1 < 0:
                digits.insert(0, 1)
            else:
                self.iterCheck(digits, k-1)