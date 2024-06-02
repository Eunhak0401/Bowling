if __name__ == '__main__':
 #점수를 입력받아 출력하는 방식이다. 문제는 점수를 몇개를 입력할지도 모른다.
 '''
 def Enter_score():
         s = "s"
         p = "p"
         m = "m"
         while True:
                 score = int(input("점수를 입력하시오: "))
                 if 1 <= score <= 10:
                         print(score)
                         return score
                 elif score == s:
                         print("10")
                         return s
                 elif score == p:
                         print("10")
                         return p
                 elif score == m:
                         print("0")
                         return m
                 elif score >= 11:
                         print("다시 입력하세요")
                 else:
                         print("다시 입력하세요")

frame = Enter_score()
set1 = 10 * frame
'''


 # 함수 안에 리스트 생성 후 그 안에 점수를 넣는 방식
 def game():
    score = []
    while True:
        print('점수를 입력하세요:', end='')
        user_input = str(input())

        if user_input == 's':
            score.append(10)
            print(score)
        elif user_input == 'p':
            score.append(10)
            print(score)
        elif user_input == '-':
            score.append(0)
            print(score)
        try:
            bowling_score = int(input(user_input))
            if 1 <= bowling_score <= 10:
                score.append(bowling_score)
                print(score)
        except ValueError:
            print("유효한 점수를 입력하세요.")

    return score

print(game())







