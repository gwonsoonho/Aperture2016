#-*-coding:utf-8 -*-

#1
list = ['Kim', 'Lee', 'Park', 'Jung']
def print_name():
    for name in list:
        print name

print print_name()

#2-1
import random

Lotto = [0,0,0,0,0,0]
print ("로또 번호를 추첨하겠습니다!")
def random_choice():
    for i in range(1,7):
        Lotto[0] = random.randrange(1,46,1)
        Lotto[1] = random.randrange(1,46,1)
        Lotto[2] = random.randrange(1,46,1)
        Lotto[3] = random.randrange(1,46,1)
        Lotto[4] = random.randrange(1,46,1)
        Lotto[5] = random.randrange(1,46,1)
random_choice()
print Lotto

#2-2
import random

Lotto = [0,0,0,0,0,0]
print ("로또 번호를 추첨하겠습니다!")

def random_choice():
    for i in range(1,7):
        Lotto[0] = random.randrange(1,46,1)
        Lotto[1] = random.randrange(1,46,1)
        Lotto[2] = random.randrange(1,46,1)
        Lotto[3] = random.randrange(1,46,1)
        Lotto[4] = random.randrange(1,46,1)
        Lotto[5] = random.randrange(1,46,1)
        if Lotto[0] == Lotto[1] or Lotto[2] or Lotto[3] or Lotto[4] or Lotto[5]:
            Lotto[0] = random.randrange(1,46,1)
        if Lotto[1] == Lotto[0] or Lotto[2] or Lotto[3] or Lotto[4] or Lotto[5]:
            Lotto[1] = random.randrange(1,46,1)
        if Lotto[2] == Lotto[1] or Lotto[0] or Lotto[3] or Lotto[4] or Lotto[5]:
            Lotto[2] = random.randrange(1,46,1)
        if Lotto[3] == Lotto[1] or Lotto[2] or Lotto[0] or Lotto[4] or Lotto[5]:
            Lotto[3] = random.randrange(1,46,1)
        if Lotto[4] == Lotto[1] or Lotto[2] or Lotto[3] or Lotto[0] or Lotto[5]:
            Lotto[4] = random.randrange(1,46,1)
        if Lotto[5] == Lotto[1] or Lotto[2] or Lotto[3] or Lotto[4] or Lotto[0]:
            Lotto[5] = random.randrange(1,46,1)

random_choice()
print Lotto

#3

def reverse(text):
    temp = ""
    for i in text:
        temp = i + temp
    return temp
print reverse("abcd")



#4

vowel = ["a", "e", "i", "o", "u"]
def anti_vowel(text):
    temp = ""
    for i in text:
        if i.lower() not in vowel:
            temp +=i

    return temp

print anti_vowel("Aperture Dimigo")

#5
def printsquare(m):
  Magic = [[0 for i in range(m)] for j in range(m)]
  r = 0
  c = m//2
  for i in range(1,m*m+1):
    Magic[r][c] = i
    br = r+1
    bc = c+1
    r = (r + m -1) % m
    c = (c + 1) % m

    if Magic[r][c] != 0:
      r = br
      c = bc-1
      print Magic[r][c]
      def magicsquare(m):
        for row in Magic:
          print ("  ".join([str(num) for num in raw]))

#6
#-*-coding:utf-8 -*-

for i in range(2,10):
    print ("%d단" % i)
    for j in range(1,10):
        print("%d * %d = %d" % (i, j, i*j))

#7
def fibo(m):
    a, b = 0, 1
    while a < m:
        print a,
        a, b = b, a+b
fibo(2000)

#8
def star(m):
    for i in range(1,m+1):
        for j in range(i,m+1):
            print "*",
        print ""

#9
def opstar(m):
    for i in range(1,m+1):
        for j in range(1,i+1):
            print "*",
        print ""
