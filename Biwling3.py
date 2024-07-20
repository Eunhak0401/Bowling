def game():
    score = []
    extra_points = []  # 숫자로 된 추가 점수 리스트
    bonus_scores = []

    print('점수 입력:', end=' ')
    user_input = input().strip()

    if user_input.lower() == 'q':
        return score, extra_points, bonus_scores

    temp_list = []
    previous_score = None
    frame_index = 0

    for char in user_input:
        if char == 'S':
            if len(score) < 10:
                temp_list.append(10)
                score.append(temp_list)
                temp_list = []
                if len(score) <= 10:
                    extra_points.append(0)  # 다음 두 점수를 추가 점수로 계산할 수 있게 초기화
                frame_index += 1
            else:
                bonus_scores.append(10)
            previous_score = 10
        elif char == 'P':
            if previous_score is not None and previous_score != 10:
                if len(score) < 10:
                    temp_list.append(10 - previous_score)
                    score.append(temp_list)
                    temp_list = []
                    if len(score) <= 10:
                        extra_points.append(0)  # 다음 한 점수를 추가 점수로 계산할 수 있게 초기화
                    frame_index += 1
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
                    frame_index += 1
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
                            frame_index += 1
            except ValueError:
                print(f"유효하지 않은 입력: {char}")

    # 점수 계산
    total_score = 0
    for i, frame in enumerate(score):
        frame_score = sum(frame)
        total_score += frame_score

    # 추가 점수 계산
    for i, extra in enumerate(extra_points):
        if i < len(score):
            if extra == 0:
                if i + 1 < len(score):
                    next_frame = score[i + 1]
                    if len(next_frame) > 0:
                        extra_points[i] += sum(next_frame)
                        if len(next_frame) == 1 and i + 2 < len(score):
                            extra_points[i] += score[i + 2][0]
            else:
                if i + 1 < len(score):
                    extra_points[i] += score[i + 1][0]

    total_extra_score = sum(extra_points)
    total_bonus_score = sum(bonus_scores)
    final_score = total_score + total_extra_score + total_bonus_score

    print(f"현재 점수 리스트: {score}")
    print(f"추가 점수 리스트: {extra_points}")
    print(f"보너스 점수 리스트: {bonus_scores}")
    print(f"점수: {total_score}")
    print(f"추가 점수 리스트 합계: {total_extra_score}")
    print(f"보너스 점수 합계: {total_bonus_score}")

    return score, extra_points, bonus_scores

# 메인
if __name__ == '__main__':
    score, extra_points, bonus_scores = game()
    total_score = sum(sum(frame) for frame in score)
    total_extra_score = sum(extra_points)
    total_bonus_score = sum(bonus_scores)
    final_score = total_score + total_extra_score + total_bonus_score

    print(f"최종 점수: {final_score}")