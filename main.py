# Course: CS30
# Period: 1
# Date created: 21/11/29
# Date last modified: 21/12/01
# Name: Xinhao Liu
# Assignment: Final Project
# Instructor: Janice Cotcher

from questions import Question
from questions import One
from questions import Two
from questions import Three
from questions import Four
from questions import Five
from questions import Six
from questions import Seven
from questions import Eight
from questions import Nine
from questions import Ten
from questions import Eleven
from questions import Twelve
from questions import Thirteen
from questions import Fourteen
from questions import Fifteen
from questions import Sixteen
from questions import Seventeen
from questions import Eighteen
from questions import Nineteen
from questions import Twenty
import feedback
print("Hi, Thank you for being here\n\nThis is just a little test for your Mental Health \n\nIn this little test you will be doing some Multiple Choice Questions\n\nTo be honest is the key!")
print("\nQuestion 1: \n")
          
#Defined function to let users to put in answers
def ans_question(current_point):
    while True: 
        #Users Input 
        answer = input("Enter your answer here: ")
        if answer == "A":
            current_point += 1
            return current_point
        elif answer == "B": 
            current_point += 2
            return current_point
        elif answer == "C":
            current_point += 3
            return current_point
        else: 
            #Warn of invalid inputs
            print("Invalid 1 Input")

current_point = 0
#Import Question's text the Questions file
One.text(Question)
#Import Question's choices the Questions file
One.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 2: \n")
#Import Question's text the Questions file
Two.text(Question)
#Import Question's choices the Questions file
Two.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 3: \n")
#Import Question's text the Questions file
Three.text(Question)
#Import Question's choices the Questions file
Three.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 4: \n")
#Import Question's text the Questions file
Four.text(Question)
#Import Question's choices the Questions file
Four.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 5: \n")
#Import Question's text the Questions file
Five.text(Question)
#Import Question's choices the Questions file
Five.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 6: \n")
Six.text(Question)
#Import Question's text the Questions file
Six.choices(Question)
#Import Question's choices the Questions file
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 7: \n")
Seven.text(Question)
#Import Question's text the Questions file
Seven.choices(Question)
#Import Question's choices the Questions file
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 8: \n")
Eight.text(Question)
#Import Question's text the Questions file
Eight.choices(Question)
#Import Question's choices the Questions file
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 9: \n")
Nine.text(Question)
#Import Question's text the Questions file
Nine.choices(Question)
#Import Question's choices the Questions file
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 10: \n")
Ten.text(Question)
#Import Question's text the Questions file
Ten.choices(Question)
#Import Question's choices the Questions file
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 11: \n")
#Import Question's text the Questions file
Eleven.text(Question)
#Import Question's choices the Questions file
Eleven.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 12: \n")
#Import Question's text the Questions file
Twelve.text(Question)
#Import Question's choices the Questions file
Twelve.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 13: \n")
#Import Question's text the Questions file
Thirteen.text(Question)
#Import Question's choices the Questions file
Thirteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 14: \n")
#Import Question's text the Questions file
Fourteen.text(Question)
#Import Question's choices the Questions file
Fourteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 15: \n")
#Import Question's text the Questions file
Fifteen.text(Question)
#Import Question's choices the Questions file
Fifteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 16: \n")
#Import Question's text the Questions file
Sixteen.text(Question)
#Import Question's choices the Questions file
Sixteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 17: \n")
#Import Question's text the Questions file
Seventeen.text(Question)
#Import Question's choices the Questions file
Seventeen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 18: \n")
#Import Question's text the Questions file
Eighteen.text(Question)
#Import Question's choices the Questions file
Eighteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 19: \n")
#Import Question's text the Questions file
Nineteen.text(Question)
#Import Question's choices the Questions file
Nineteen.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
print("\nQuestion 20: \n")
#Import Question's text the Questions file
Twenty.text(Question)
#Import Question's choices the Questions file
Twenty.choices(Question)
ans_question(current_point)
#Calculate points that the use earned after their input
#After the use finished all the questions give feedback based on their current points
feedback.give_feedback(current_point)



       

        
            


    
    