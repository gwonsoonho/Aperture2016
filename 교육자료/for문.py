"""
For Aperture 2016 Python study
제작 : HD14 김민성

for 문

"""

#1.For과 range
"""
C언어
#include <stdio.h>
int main(){
    for(int i = 0; i < 5; i++){
        printf("hello");
    }
    return 0;
}
"""
for i in range(0,5):
    print "hello"



#2.For과 list
list = ['Aperture', 'Club', 'Slaves']
for slave in list:
    print "%s is slave" % slave



#3.For과 tuple
tuple = ('Naver', 'Google', 'Nate')
for Engine in tuple:
    print "%s is my engine" % tuple
