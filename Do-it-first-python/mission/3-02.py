# 변수 score에 학생의 점수를 입력받으세요
score = int(input())

# 점수에 따라 성적을 출력하는 프로그램을 만들어 보세요
if score >= 88:
    print('A+')
elif score >= 77:
    print('A0')
elif score == 0:
    print('F')
else:
    print('B+')
