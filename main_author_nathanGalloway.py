#_author_
#Nathan Galloway
#main.py
#11/4/21
#gym needs/goals
#the purpose of this program i created is to make a platform to help every
#level of fitness.The amazing part of this program is that is works for all
#sports from cardio to resestance training. It is sad knowing that a majority
#of fitnessed supplamets is unkown of by  majority of athletes. this program
#help athletes increase their preformance and strength. it seems that
#supplaments are more known of in the gym with the power lifters and the body
#builders, but i want help spread out the benifits of sport nutrition and
#suppluments.
print("section 1")
print("this section will recomend some supplaments you should take.")
print("Welcome, what is your name", end='?')
name = input()
print("My name is", name)
print("hi", name, "we will determine your fitness info shortly")
print("what is your age", end='?')
age = str(input())
print("my age is",age)
if 18 <= int(age) < 50:
    print("Hey",name,"you should take some pre-workout and creatine")
elif int(age)>=50:
    print("Hey",name,"your should take some test boosters")
else:
    print("Hey",name,"you should take some creatine")
#
#this section above uses variables and if else statemetns to asses what the
#user should take. it is simple now, but a work in progress.
#
print("section 2")
print("this next section is going to be imormative about fitness supplaments")
print("these next questions you will be given the answers too for a better "
      "understanding")
print("true or false. Are whey and isolate protein the same diet wise"
      , end='?')
whey = "low cal protein"
isolate = "extreme low cal protein"
print(bool(whey == isolate))
print("isolate is less calories")
print("true or false. whey and isolate protein work differntly", end='.')
whey1 = "fast absorbing protein."
isolate1= "fast absorbing protein."
print(bool(whey1 == isolate1))
print("true of false. Both whey and isolate are fast absorbing proteins"
      , end='.')
print(bool(whey1 == isolate1))
eleca = True
amino = not False
print("true of false. electralights hydrate and aminos recover your body"
      , end='.')
print(bool(eleca and amino))
print("true or false. creatine increases atp or pre workout muscle growth"
      , end='.')
preworkout = False
creatine = True
print(bool(preworkout or creatine))
print("although true, pre workout does not increase strengh but does "
      "increase endurane and atp output")
#
#section two uses bool to feed information in a more interaftive way rather
#then just a list of print statements
#
print("section 3")
print("determin how many hours you should be at the gym")
print("how many hours do you work out a day on average", end='.')
hour = int(input())
time = 2
i=1
while hour < time:
    print("your should increase your time in the gym by 1")
    hour += 1
else:
    print("perfect amount, just don't stay past 3 hours a day")
#
#section 3 uses while loop to let the user figure out the amount of hours they
# should work out
#
print("section 4")
print("some supplaments you take before your lifts are, pre-workout, "
      "creatine, muti vitamin, and fishoils")
print("how many minutes do you take your supplaments before your workout"
      , end='?')
pretime = input()
for pretime in range(int(pretime), 31):
    if pretime != 30:
        print("incorrect")
    print(pretime)
else:
    print("correct you should take 30 mins prior to working out")
#
#section 4 uses 4 loops to get the user to understand how early they should
#take pre gym supplamets before attending the gym.
#
print("section 5, thanks")
def greet(name, thanks="thanks for learing fitness facts with us, hope to see "
                       "you soon when updated woth the nutrition side of the "
                       "program!"):
    print("hey!", name + ',' + thanks)
greet(name)
print("section 6")
print("links that helped me")
#
#section 5 is the ending section used to greet and thank the user for attending
#
#https://www.programiz.com/python-programming/function-argument
#https://www.w3schools.com/python/python_for_loops.asp
#https://www.programiz.com/python-programming/operators
#https://www.youtube.com/watch?v=9OK32jb_TdI
#https://www.programiz.com/python-programming/if-elif-else
#https://www.w3schools.com/python/python_while_loops.asp
#https://realpython.com/python-boolean/
#https://www.youtube.com/watch?v=r526yum0EYQ&t=102s
#https://www.programiz.com/python-programming/while-loop
#
#i enjoyed this project, i had a hard time with connecting one thin got another
#but because i was on my own i had to do trial an error until i got it ot work
#how i liked. i deffently improved my coding skills by doing this project
#