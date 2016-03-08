"""
For Aperture 2016 Python study
제작 : HD14 김민성

If 문

"""

#1. 기본적인 if문

Aperture = 15
if Aperture > 10:
    print "Club!"


#2. if, else
Club = 12
if Club > 10:
    print "yes!"
else:
    print "No!"

#3. if, elif, else

grade = 2
if grade ==1:
    print "very good!"
elif grade >1 or grade <=4:
    print "good"
elif grade >4 or grade <6:
    print "soso"
else:
    print "bad"
