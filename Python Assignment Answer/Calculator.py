#-*-coding : utf-8 -*-

def add(a, b):
    print ("당신이 원하는 결과값은 %d입니다." % a+b)
    print ("계속하시려면 y를 쳐주세요.")
    in = input()
    if in == 'y':
        continue
    else:
        break

def minu(a, b):
    print ("당신이 원하는 결과값은 %d입니다." % a-b)
    print ("계속하시려면 y를 쳐주세요.")
    in = input()
    if in == 'y':
        continue
    else:
        break

def gob(a, b):
    print ("당신이 원하는 결과값은 %d입니다." % a*b)
    print ("계속하시려면 y를 쳐주세요.")
    in = input()
    if in == 'y':
        continue
    else:
        break

def div(a, b):
    print ("당신이 원하는 결과값의 몫은 %d이고 나머지는 %d입니다." % (a%b, a/b))
    print ("계속하시려면 y를 쳐주세요.")
    in = input()
    if in == 'y':
        continue
    else:
        break

print ("두 수를 입력하세요.")
a, b = input()
while True:
    print ("더하기를 하시려면 1번, 빼기를 하시려면 2번 곱하기를 하시려면 3번, 나누기를 하시려면 4번을 쳐주세요")
    num = input()
    if num == 1:
        add(a,b)
    elif num == 2:
        minu(a,b)
    elif num == 3:
        gob(a,b)
    elif num == 4:
        div(a,b)
    else:
        print ("다시입력해주세요.")
        continue
