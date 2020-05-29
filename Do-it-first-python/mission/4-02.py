# 도마뱀 빌이 장바구니에 담은 과일 리스트입니다
fruits = ['바나나', '딸기', '두리안', '망고']

# '딸기'가 fruits 안에 들어 있다면 지우고, 없다면 메시지를 출력하세요
if '딸기' in fruits:
    fruits.remove('딸기')
else:
    print('딸기는 fruits 안에 없습니다!')
