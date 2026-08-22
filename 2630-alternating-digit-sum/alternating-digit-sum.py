class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0

        for i in range(len(str(n))):
          if i % 2 == 0:
            answer += int(str(n)[i])
          else:
            answer -= int(str(n)[i])

        return answer      