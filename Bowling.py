def game():
    score = []
    extra_scores = []

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
            # 점수 'S' 눌리면 리스트에 10점 추가
            temp_list.append(10)
            score.append(temp_list)
            temp_list = []
            previous_score = None
            # 안할시 'S'가 들어간 리스트가 있을시 10프레임이 넘어도 리스트가 추가됨.
            if len(score) >= 10:
                break
            # 'P'가 눌리면 10 - 그 전 숫자를 하여 리스트안 점수 추가
        elif char == 'P':
            if previous_score is not None:
                temp_list.append(10 - previous_score)
                previous_score = 10 - previous_score
                score.append(temp_list)
                temp_list = []
                if len(score) >= 10:
                    break
                # '-'가 눌리면 리스트에 0점 추가
        elif char == '-':
            temp_list.append(0)
            previous_score = 0
            if len(temp_list) == 2:
                score.append(temp_list)
                temp_list = []
                if len(score) >= 10:
                    break
        else:
            # 리스트 안 숫자점수 추가
            try:
                bowling_score = int(char)
                if 0 <= bowling_score <= 10:
                    temp_list.append(bowling_score)
                    previous_score = bowling_score

            except ValueError:
                print(f"유효하지 않은 입력: {char}")

                # 10프레임까지, 10프레임이 넘어가면 점수 추가 안됨.
                if len(score) >= 10:
                    break

                # 2개씩 끊어서 리스트에 추가
                for i in range(0, len(temp_list), 2):
                    score.append(temp_list[i:i + 2])


                # 남은 temp_list 추가 (기존 프레임이 꽉 차지 않은 경우)
                if temp_list and len(score) < 10:
                    score.append(temp_list)

                    # 추가 프레임 생성
                    if len(temp_list) > 0:
                        score.append(temp_list[:2])  # 두 점수만 추가

                    extra_scores.extend(temp_list)

                elif sum(last_frame) == 10 and len(last_frame) == 2:  # 마지막 프레임이 스페어인 경우
                    next_char = user_input[len(user_input) - 1]
                    if next_char == 'S':
                        extra_scores.append(10)
                    elif next_char == '-':
                        extra_scores.append(0)
                    else:
                        try:
                            extra_scores.append(int(next_char))
                        except ValueError:
                            print(f"유효하지 않은 입력: {next_char}")


                    # 10프레임이 넘어가면 추가 점수 처리
                    if len(score) == 10:
                        temp_list = score[-1]
                        if temp_list == [10]:  # 마지막 프레임이 스트라이크인 경우
                            temp_list = []
                            for char in user_input[len(user_input) - 2:]:  # 마지막 두 문자를 확인
                                if char == 'S':
                                    temp_list.append(10)
                                elif char == 'P':
                                    if previous_score is not None:
                                        temp_list.append(10 - previous_score)
                                elif char == '-':
                                    temp_list.append(0)
                                else:
                                    try:
                                        bowling_score = int(char)
                                        if 0 <= bowling_score <= 10:
                                            temp_list.append(bowling_score)
                                    except ValueError:
                                        print(f"유효하지 않은 입력: {char}")

                            extra_scores.extend(temp_list)

                        elif sum(last_frame) == 10 and len(last_frame) == 2:  # 마지막 프레임이 스페어인 경우
                            next_char = user_input[len(user_input) - 1]
                            if next_char == 'S':
                                extra_scores.append(10)
                            elif next_char == '-':
                                extra_scores.append(0)
                            else:
                                try:
                                    extra_scores.append(int(next_char))
                                except ValueError:
                                    print(f"유효하지 않은 입력: {next_char}")


    # 현재 점수 합계 계산
    total_score = sum(sum(pair) for pair in score)
    total_extra_score = sum(extra_scores)

    print(f"현재 점수 리스트: {score}")
    print(f"추가 점수 리스트: {extra_scores}")
    print(f"점수: {total_score}")
    print(f"추가 점수 합계: {total_extra_score}")

    return score, extra_scores

# 메인
if __name__ == '__main__':
    final_score, extra_scores = game()
    total_final_score = sum(sum(pair) for pair in final_score)
    total_extra_score = sum(sum(pair) for pair in extra_scores)






