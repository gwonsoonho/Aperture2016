#-*- coding: utf-8 -*-
#숙제 1일차 답안.py
a = 10
print "숫자 맞추기 게임입니다."
while True:

    g = input("숫자를 입력하세요 : ")
    if a > g:
        print "숫자가 작습니다.다른 숫자를 입력해 보세요"
    elif a == g:
        print "맞췄습니다! 게임을 끝내겠습니다."
        break
    else:
        print "숫자가 큽니다. 다른 숫자를 입력해 보세요"