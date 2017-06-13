name = raw_input("What's your name?")
print ("Hi " + name + "!")


answer_dict = {}
quiz_dict = {}


answer_dict["easy"] = ["Buzz Aldrin", "West Point", "MIT", "astronaut"]
answer_dict["medium"] = ["Moon rocks", "Apollo", "Soviet Luna", "moon's"]   
answer_dict["hard"] = ["Saturn", "62", "moons", "Titan"]    

answer_holders = ["__1__", "__2__", "__3__", "__4__"]


quiz_dict["easy"] = answer_holders[0] + " is famously the second human to walk on the moon. When " + answer_holders[0] + " graduated from high school he went on to become third in his class at" + answer_holders[1] + ". They would become a fighter pilot before completing their education in gradute school at " + answer_holders[2] + " before moving on to become an " +  answer_holders[3] + "." 
quiz_dict["medium"] = answer_holders[0] + " on earth come from three sources: those collected by the" + answer_holders[1] + "missions, those collected by the" + answer_holders[2] + "missions and those that were ejected from the  " + answer_holders[3] + "surface. " + answer_holders[0] + " in the U.S. are considered to be national treasure and are illegal to sell within its borders."
quiz_dict["hard"] =answer_holders[0] + " has a total of " + answer_holders[1] + " " + answer_holders[2] + " . The largest is named " + answer_holders[3] + " which is believed to make up 96 percent of the matter orbiting " + answer_holders[0] + " . " + answer_holders[3] + " is believed to be one of two " + answer_holders[2] + " its size, but the other one broke up and contributed to creating some of the debris that formed the very distinctive shapes around " + answer_holders[0] + " ." 


choice = raw_input("welcome to the quiz. you will have 5 chances to get the answers correct. please choose your difficulty level: easy, medium or hard")
level = choice

def get_level(choice, quiz_dict, answer_dict):
    global level
    if level == "easy" or "medium" or "hard":
        print quiz_dict[level]
    else:
        level = "easy"
        print "i did not understand your response. defaulting to level easy"
        print quiz_dict[level]
get_level(choice, quiz_dict, answer_dict)
            

def replace_quiz_dict(answer, quiz_dict, index):
    counter = 0
    level = choice
    for pos in quiz_dict[level]:
        if pos == answer_holders[index]:
            quiz_dict[level][counter] = answer
        counter += 1
            
            
def answering_quiz():
    index = 0
    failed = 0
    right_answers = 0
    wrong_answers = 0
    replacement = []
    level = choice
    
    for correct_answer in answer_dict[level]:
        #split into a list
        quiz_dict[level] = quiz_dict[level].split()
        #they are now ansering the next blank
        answering = 0
        while answering == 0 and failed == 0:
            if right_answers == 4:
                    print "winner winner chicken dinner. quiz is terminated"
            else:        
            #get user input for answer
                answer = raw_input("please fill in the blank for item " + str(index + 1))
            
            #if so see line 54, if not see line 64
            if failed == 0 and answer == correct_answer:
                print "correct!"
                answering = 1
                right_answers += 1
                replace = replace_quiz_dict(correct_answer, quiz_dict, index)
                quiz_dict[level] = " ".join(quiz_dict[level])
                print quiz_dict[level]
                index += 1
                if right_answers == 4:
                    print "winner winner chicken dinner. quiz is terminated"
            else:
                print "baum baum baum baaaaauuuuummmmm...wrong answer..."
                wrong_answers += 1
                print "you have gotten " + str(wrong_answers) + " answers wrong. you have " + str(5 - wrong_answers) + " tries left."
                answering = 1
                if wrong_answers == 5:
                    print "game over"
                    failed = 1
                    answering = 1
print answering_quiz()                  
