if __name__ == '__main__':

 # 함수 안에 리스트 생성 후 그 안에 점수를 넣는 방식
 def game():
     score = []
     while True:
         print('점수를 입력하세요:', end=' ')
         user_input = input().strip()

         for char in user_input:
             if char == 'S':
                 score.append(10)
             elif char == 'P':
                 score.append(10)
             elif char == '-':
                 score.append(0)
             else:
                 try:
                     bowling_score = int(char)
                     if 1 <= bowling_score <= 10:
                         score.append(bowling_score)
                     else:
                         print(f"점수 {bowling_score}은(는) 1에서 10 사이여야 합니다.")
                 except ValueError:
                     print(f"유효하지 않은 입력: {char}")

         result = sum(score)
         print(result)

     return score


 print(game())







