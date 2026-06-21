class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = '' 
        for num in digits:
            num_str += str(num) 
        num = str(int(num_str) + 1)
        return [int(n) for n in num]
        
        