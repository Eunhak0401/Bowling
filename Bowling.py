# 함수로 만들어 간단하게 쓰기
def game():
    score = []

    print('점수 입력:', end=' ')
    user_input = input().strip()

    if user_input.lower() == 'q':
        return score

    # 리스트 만들기
    temp_list = []
    previous_score = None

    # 점수 입력 후 리스트에 점수 추가
    for char in user_input:
        if char == 'S':
            temp_list.append(10)
            score.append(temp_list)
            temp_list = []
            previous_score = None
            # 'P'가 눌리면 10 - 그 전 숫자를 하여 리스트안 점수 추가
        elif char == 'P':
            if previous_score is not None:
                temp_list.append(10 - previous_score)
                # '-'가 눌리면 리스트에 0점 추가
        elif char == '-':
            temp_list.append(0)
            previous_score = 0
        else:
            # 리스트 안 숫자점수 추가
            try:
                bowling_score = int(char)
                if 1 <= bowling_score <= 10:
                    temp_list.append(bowling_score)
                    previous_score = bowling_score

            except ValueError:
                print(f"유효하지 않은 입력: {char}")

                # 'S'가 있는 경우 다음 두 개의 점수를 추가
                # 현재 문제있음 적용x
                '''
                result_score = score[:]
                for i, val in enumerate(score):
                    if val == 10:
                        if i + 2 < len(score) and (score[i] == 10 and (i == 0 or score[i - 1] != 10)):  # 'S' 처리
                            result_score[i] += score[i + 1] + score[i + 2]
                        elif i + 1 < len(score) and (score[i] == 10 and (i > 0 and score[i - 1] == 10)):  # 'P' 처리
                            result_score[i] += score[i + 1]
                            '''

    # 2개씩 끊어서 리스트에 추가, 현재 'S', 'P', '-'를 치면 리스트의 2개 이상 들어가는 오류가 있음.
    for i in range(0, len(temp_list), 2):
        score.append(temp_list[i:i + 2])

        # 10프레임까지, 10프레임이 넘어가면 점수 추가 안됨.
        if len(score) >= 10:
            break

    # 현재 점수 합계 계산
    total_score = sum(sum(pair) for pair in score)
    print(f"현재 점수 리스트: {score}")
    print(f"점수: {total_score}")


    return score

# 메인
if __name__ == '__main__':
    final_score = game()
    total_final_score = sum(sum(pair) for pair in final_score)






