def game():
    score = []

    print('점수 입력:', end=' ')
    user_input = input().strip()

    if user_input.lower() == 'q':
        return score

    temp_list = []
    previous_score = None

    for char in user_input:
        if char == 'S':
            temp_list.append(10)
            score.append(temp_list)
            temp_list = []
            previous_score = None
        elif char == 'P':
            if previous_score is not None:
                temp_list.append(10 - previous_score)
        elif char == '-':
            temp_list.append(0)
            previous_score = 0
        else:
            try:
                bowling_score = int(char)
                if 1 <= bowling_score <= 10:
                    temp_list.append(bowling_score)
                    previous_score = bowling_score

            except ValueError:
                print(f"유효하지 않은 입력: {char}")

    # 2개씩 끊어서 리스트에 추가
    for i in range(0, len(temp_list), 2):
        score.append(temp_list[i:i + 2])
        # 10프레임까지
        if len(score) >= 10:
            break

    # 현재 점수 합계 계산
    total_score = sum(sum(pair) for pair in score)
    print(f"현재 점수 리스트: {score}")
    print(f"점수: {total_score}")


    return score


if __name__ == '__main__':
    final_score = game()
    total_final_score = sum(sum(pair) for pair in final_score)






