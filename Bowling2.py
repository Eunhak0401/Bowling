def calculate_score(score_board, extra_points): # 점수계산 함수
    total_score = 0
    frame_scores = [0] * 10 # 각 프레임의 점수 저장 리스트

    for i in range(10):
        frame_score = 0
        if score_board[i][0] == 'S':  # 스트라이크
            frame_score = 10
            if i < 9:
                next_frame = score_board[i + 1]
                if next_frame[0] == 'S':  # 다음 프레임도 스트라이크
                    frame_score += 10 # 10점 추가
                    if i + 2 < 10: # 다음 다음 프레임이 존재하면
                        next_next_frame = score_board[i + 2]
                        frame_score += 10 if next_next_frame[0] == 'S' else int(next_next_frame[0].replace('-', '0'))
                    else:
                        frame_score += 10 if score_board[9][1] == 'S' else int(score_board[9][1].replace('-', '0'))
                else: # 다음 프레임이 스트라이크가 아니면
                    frame_score += int(next_frame[0].replace('-', '0'))
                    if next_frame[1] == 'P': # 스페어일때
                        frame_score += 10 - int(next_frame[0].replace('-', '0'))
                    else: #숫자일때
                        frame_score += int(next_frame[1].replace('-', '0'))
            else:  # 10번째 프레임
                frame_score += 10 if score_board[i][1] == 'S' else int(score_board[i][1].replace('-', '0'))
                frame_score += 10 if score_board[i][2] == 'S' else (10 - int(score_board[i][1].replace('-', '0')) if score_board[i][2] == 'P' else int(score_board[i][2].replace('-', '0')))
        elif score_board[i][1] == 'P':  # 스페어일때
            frame_score = 10 # 10점 추가
            if i < 9: # 10번째 프레임이 아니면
                next_frame = score_board[i + 1]
                frame_score += 10 if next_frame[0] == 'S' else int(next_frame[0].replace('-', '0'))
            else:  # 10번째 프레임이면
                frame_score += 10 if score_board[i][2] == 'S' else (10 - int(score_board[i][0].replace('-', '0')) if score_board[i][2] == 'P' else int(score_board[i][2].replace('-', '0')))
        else: # 일반 프레임
            frame_score = int(score_board[i][0].replace('-', '0')) + int(score_board[i][1].replace('-', '0'))

        frame_scores[i] = frame_score # 점수 저장

    for frame_score in frame_scores:
        total_score += frame_score # 점수 계산

    return total_score

def print_score_board(score_board, extra_points): # 점수판 함수
    # 점수판 출력
    for i in range(10):
        frame = score_board[i]
        if i == 9: # 10프레임
            print(f"{frame[0]:>2} {frame[1]:>2} {frame[2]:>2}", end=' | ')
        else: # 1 ~ 9프레임
            print(f"{frame[0]:>2} {frame[1]:>2}", end=' | ')
    print()

    # 추가 점수 출력
    for i in range(10):
        extra = extra_points[i]
        if i == 9:  # 10프레임
            print(f"{extra:>2}", end = '       | ')
        else: # 1~9프레임
            print(f"{extra:>2}", end='    | ')
    print()

def update_extra_points(score_board, extra_points): # 추가점수 함수
    for i in range(10):
        if score_board[i][0] == 'S':  # 스트라이크
            next_two_rolls = []
            if i < 9:
                next_frame = score_board[i + 1]
                next_two_rolls.append(10 if next_frame[0] == 'S' else int(next_frame[0].replace('-', '0')))
                if next_frame[0] == 'S' and i + 2 < 10:
                    next_next_frame = score_board[i + 2]
                    next_two_rolls.append(10 if next_next_frame[0] == 'S' else int(next_next_frame[0].replace('-', '0')))
                else:
                    if next_frame[1] == 'S':
                        next_two_rolls.append(10)
                    else:
                        next_two_rolls.append(10 if next_frame[1] == 'P' else int(next_frame[1].replace('-', '0')))
            else:  # 10번째 프레임
                next_two_rolls.append(10 if score_board[i][1] == 'S' else int(score_board[i][1].replace('-', '0')))
                if score_board[i][2] == 'P':
                    next_two_rolls.append(10 - int(score_board[i][1].replace('-', '0')))
                else:
                    next_two_rolls.append(10 if score_board[i][2] == 'S' else int(score_board[i][2].replace('-', '0')))
            extra_points[i] = str(10 + sum(next_two_rolls[:2]))

        elif score_board[i][1] == 'P':  # 스페어
            if i < 9:
                next_frame = score_board[i + 1]
                extra_points[i] = str(10 + (10 if next_frame[0] == 'S' else int(next_frame[0].replace('-', '0'))))
            else:  # 10번째 프레임
                extra_points[i] = str(10 + (10 if score_board[i][2] == 'S' else int(score_board[i][2].replace('-', '0'))))
        else:
            # 단순한 점수 입력의 경우, 추가 점수는 두 점수를 합한 값으로 설정
            frame_score = int(score_board[i][0].replace('-', '0')) + int(score_board[i][1].replace('-', '0'))
            extra_points[i] = str(frame_score)

def game():
    score_board = [['-', '-', '-'] for _ in range(10)]
    extra_points = ['' for _ in range(10)]
    frame_index = 0
    roll = 0

    while frame_index < 10:
        if frame_index == 9: # 10프레임이라면
            if roll == 0: # 10프레임 첫 번째 점수
                print(f"10번째 프레임 첫 번째 점수 입력:", end=" ")
            elif roll == 1: # 두 번째 점수
                print(f"10번째 프레임 두 번째 점수 입력 :", end=" ")
            else: # 세 번째 점수
                print(f"10번째 프레임 세 번째 점수 입력 :", end=" ")
        else: # 10프레임이 아니라면
            print(f"프레임 {frame_index + 1} {'첫 번째' if roll == 0 else '두 번째'} 점수 입력:", end=" ")

        char = input().strip()



        if char == 'S' and roll == 0: # 스트라이크, 첫 번째 점수라면
            score_board[frame_index][roll] = 'S' # 문자 S를 추가
            if frame_index == 9: # 프레임 10이라면
                roll += 1 # 자리 2개 추가
            else:
                roll = 0 # 자리 1개 추가
                frame_index += 1
        elif frame_index == 9 and char == 'S' and roll > 0: # 10프레임에서 스트라이크, 두 번쨰 자리 이상이라면
            score_board[frame_index][roll] = 'S' # 문자 S를 추가
            roll += 1
        elif frame_index == 9 and char == 'P' and roll > 0: # 10프레임에서 스페어, 두 번째 자리 이상이라면
            if roll == 1 and score_board[frame_index][0] == 'S':
                print("유효하지 않은 입력입니다. 다시 입력해주세요.")
                continue
            score_board[frame_index][roll] = 'P' # 문자 P를 추가
            roll += 1
        elif char == 'P' and roll == 1 and score_board[frame_index][0] != 'S': # P, 두 번째 자리가 1이라면, S가 아니라면
            score_board[frame_index][roll] = 'P' # 문자 P추가
            roll = 0
            frame_index += 1
        elif char == '-' or char.isdigit(): # 문자 -라면
            if char == '-':
                score_board[frame_index][roll] = '-' # 문자 - 추가
            else:
                score_board[frame_index][roll] = char

            if frame_index == 9: # 10프레임일때
                roll += 1 # 자리 추가
            else:
                if roll == 1 or (roll == 0 and score_board[frame_index][0] == 'S'):
                    roll = 0
                    frame_index += 1
                else:
                    roll += 1
        else:
            print("유효하지 않은 입력입니다. 다시 입력해주세요.")
            continue

        # 점수판 및 추가 점수 업데이트
        update_extra_points(score_board, extra_points)
        print_score_board(score_board, extra_points)

        # 현재 점수 계산
        total_score = calculate_score(score_board, extra_points)
        print(f"현재 점수: {total_score}")

        # 10프레임에서 세 번째 점수를 입력한 후 게임 종료
        if frame_index == 9 and roll == 3:
            break
        # 10프레임에서 첫 번째 문자가 'S'가 아니면 게임 종료
        if frame_index == 9 and roll == 1 and char != 'S':
            break

    # 출력
    print("게임 종료")
    print_score_board(score_board, extra_points)
    final_score = calculate_score(score_board, extra_points)
    print(f"최종 점수: {final_score}")

# 메인
if __name__ == '__main__':
    game()