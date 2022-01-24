
def give_feedback(current_point):
        if current_point <= 20: 
            feedback1()
        elif current_point > 20 and current_point <= 40:
            feedback2()
        elif current_point > 40 and current_point <= 60:
            feedback3()

def feedback1():
    suggestion = {"\n1.Professional Healthcare":
                  {"You can go to the website 'http://www.camh.ca'\n"},
                  "2.Talk with your family friend":
                  {"Don't be afraid to share your story\n"},
                  "3.Change your way of thinking":
                  {"It is hard but you should try to think positively\
                  \nand tell yourself believe in your self that you can\
                  \nfix those problems\n"
                 }}
    for ways in suggestion:
        print(f"{ways}")
        for item in suggestion[ways]:
            print(f"{item}")

def feedback2():
    print("You are now in the middle of the bridge, make more friends, find things to do that will relax you, and don't get too hung up on unhappy things.")

def feedback3():
    print("You are a very healthy person, enjoy your life!")

