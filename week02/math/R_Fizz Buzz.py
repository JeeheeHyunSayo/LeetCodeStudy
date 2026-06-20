'''
Q. 3,5,15의 배수일 때만 다른 값 출력하기
A. 3,5,15로 나눴을 때 나머지가 0인 경우에만 특정 문자열 출력, 이외에는 숫자를 문자열 형식으로 출력하기
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res