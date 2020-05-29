# 치즈 접시가 비어 있어요
cheeze = []

# 치즈 접시에 문자열 '치즈'가 무한으로 추가되고, 그때마다 '치즈 추가!'를 출력해요
while True:
    cheeze.append('치즈')
    print('치즈 추가!')

# cheeze 속 치즈가 50개가 되면 추가를 멈추고 '아이~ 배불러!'를 출력해요
    if len(cheeze) == 50:
        print('아이~ 배불러!')
        break
    
