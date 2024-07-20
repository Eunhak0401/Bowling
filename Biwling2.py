def game():
    score = []
    extra_scores = []
    bonus_scores = []

    print('점수 입력:', end=' ')
    user_input = input().strip()

    if user_input.lower() == 'q':
        return score, extra_scores, bonus_scores

    # 리스트 만들기
    temp_list = []
    previous_score = None

    # 점수 입력 후 리스트에 점수 추가
    for char in user_input:
        if char == 'S':
            # 점수 'S' 눌리면 리스트에 10점 추가
            if len(score) < 10:
                temp_list.append(10)
                score.append(temp_list)
                temp_list = []
            else:
                bonus_scores.append(10)
            previous_score = None
        elif char == 'P':
            if previous_score is not None:
                if len(score) < 10:
                    temp_list.append(10 - previous_score)
                    score.append(temp_list)
                    temp_list = []
                else:
                    bonus_scores.append(10 - previous_score)
                previous_score = 10 - previous_score
        elif char == '-':
            if len(score) < 10:
                temp_list.append(0)
                previous_score = 0
                if len(temp_list) == 2:
                    score.append(temp_list)
                    temp_list = []
            else:
                bonus_scores.append(0)
        else:
            try:
                bowling_score = int(char)
                if 0 <= bowling_score <= 10:
                    if len(score) < 10:
                        temp_list.append(bowling_score)
                        previous_score = bowling_score
                        if len(temp_list) == 2:
                            score.append(temp_list)
                            temp_list = []
                    else:
                        bonus_scores.append(bowling_score)
            except ValueError:
                print(f"유효하지 않은 입력: {char}")

    # 현재 점수 합계 계산
    total_score = sum(sum(pair) for pair in score)
    total_extra_score = sum(extra_scores)

    print(f"현재 점수 리스트: {score}")
    print(f"추가 점수 리스트: {extra_scores}")
    print(f"보너스 점수 리스트: {bonus_scores}")
    print(f"점수: {total_score}")
    print(f"추가 점수 합계: {total_extra_score}")

    return score, extra_scores, bonus_scores

# 메인
if __name__ == '__main__':
    final_score, extra_scores, bonus_scores = game()
    total_final_score = sum(sum(pair) for pair in final_score)
    total_extra_score = sum(extra_scores)
    total_bonus_score = sum(bonus_scores)
    print(f"최종 점수: {total_final_score + total_extra_score + total_bonus_score}")