class Solution:
    def countEven(self, num: int) -> int:
        answer =0

        for i in range(1, num + 1):
            digit_sum = 0

            for digit in str(i):
                digit_sum += int(digit)

            if digit_sum % 2 == 0:
             answer += 1

        return answer
         