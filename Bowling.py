def game():
    score = []  # 현재 점수 리스트를 감싸고 있는 리스트
    extra_points = []  # 추가 점수 리스트
    bonus_scores = []  # 보너스 점수 리스트

    print('점수 입력:', end=' ')
    user_input = input().strip()

    temp_list = []  # 현재 점수 리스트
    previous_score = 0

    for char in user_input:
        if char == 'S':
            if len(score) < 10:
                temp_list.append(10)
                score.append(temp_list)
                temp_list = []
            # 10프레임이 넘어가면 보너스 점수 리스트에 추가
            else:
                bonus_scores.append(10)
            previous_score = 10
        elif char == 'P':
            # 'P'는 한 리스트 안에 합이 10이므로 '처음 점수가 10이 아니라면' 조건을 붙인다.
            if previous_score != 10:
                if len(score) < 10:
                    temp_list.append(10 - previous_score)
                    score.append(temp_list)
                    temp_list = []
                else:
                    bonus_scores.append(10 - previous_score)
                previous_score = 10
        elif char == '-':
            if len(score) < 10:
                temp_list.append(0)
                if len(temp_list) == 2:
                    score.append(temp_list)
                    temp_list = []
            else:
                bonus_scores.append(0)
            previous_score = 0
        else:
            try:
                bowling_score = int(char)
                if 0 <= bowling_score <= 10:
                    if len(score) < 10:
                        temp_list.append(bowling_score)
                        # 리스트 하나에 점수 2개 초과시 새로운 리스트 생성
                        if len(temp_list) == 2:
                            score.append(temp_list)
                            temp_list = []
                    else:
                        bonus_scores.append(bowling_score)
                    previous_score = bowling_score
            except ValueError:
                print(f"유효하지 않은 입력: {char}")

    # 점수 계산
    total_score = 0
    for i, frame in enumerate(score):
        frame_score = sum(frame)
        total_score += frame_score

    # 추가 점수 계산
    for i, frame in enumerate(score):
        # 프레임의 합이 10인지 확인
        if sum(frame) == 10:
            if frame[0] == 10:  # 스트라이크일때
                # 다음 프레임 존재 여부 확인
                if i + 1 < len(score):
                    next_frame = score[i + 1]
                    extra_points.append(next_frame[0])
                    if len(next_frame) > 1:
                        extra_points.append(next_frame[1])
                    elif i + 2 < len(score):
                        extra_points.append(score[i + 2][0])
                if i == 8:  # 9번째 프레임이 스트라이크일 때만 보너스 점수 추가
                    if len(bonus_scores) > 0:
                        extra_points.append(bonus_scores[0])
            elif len(frame) > 1 and sum(frame) == 10:  # 스페어일때
                if i + 1 < len(score):
                    next_frame = score[i + 1]
                    extra_points.append(next_frame[0])

    # 점수 출력
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
    total_extra_score = sum(point for point in extra_points if point is not None)
    total_bonus_score = sum(bonus_scores)
    final_score = total_score + total_extra_score + total_bonus_score

    print(f"최종 점수: {final_score}")