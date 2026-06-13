import random as rd 
import time

questions_set={
    "Who is the Prime Minister of India?":("narendra modi","rahul gandhi","amit shah","nitin gadkari"),
    "What is the currency of India":("rupee","dollar","euro","yen"),
    "What is the capital of India":("new delhi","mumbai","chennai","kolkata"),
    "What is the largest state of India":("rajasthan","gujarat","maharashtra","delhi"),
    "What is the smallest state of India":("goa","gujarat","maharashtra","delhi"),
    "What is the most populous state of India":("uttar pradesh","maharashtra","delhi","karnataka"),
    "What is the least populous state of India":("sikkim","delhi","bangalore","kolkata")
    }

answer_set={
    "Who is the Prime Minister of India?":"narendra modi",
    "What is the currency of India":"rupee",
    "What is the capital of India":"new delhi",
    "What is the largest state of India":"rajasthan",
    "What is the smallest state of India":"goa",
    "What is the most populous state of India":"uttar pradesh",
    "What is the least populous state of India":"sikkim"
    }

t1=time.perf_counter()
score=0
time_limit=10

unasked_questions = list(questions_set.keys())

while unasked_questions:
    q = rd.choice(unasked_questions)
    unasked_questions.remove(q)
    print(q)
    
    # We use rd.sample here because questions_set[q] is a tuple (which is immutable)
    # rd.sample(..., 4) will return a randomly shuffled list of the 4 options
    op=list(rd.sample(questions_set[q], 4))
    for i, option in enumerate(op, start=1):
        print(i,".", option)
    qt1=time.perf_counter()    
    ans=int(input("enter your option number: "))
    qt2=time.perf_counter()
    if ans<0 or ans>4:
        raise ValueError("Invalid option")
    if ans==op.index(answer_set[q])+1 and int(qt2-qt1)<=time_limit:  
        print("Correct Answer")
        score+=1
    elif int(qt2-qt1)>time_limit:
        print("Time out")
        break
    elif ans!=op.index(answer_set[q])+1:
        print("Incorrect Answer")
        print("Correct Answer is",answer_set[q])
        break
    if score==len(questions_set):
        print("You have answered all the questions correctly")
        break
t2=time.perf_counter()
print("Your final score is",score)
print("Your total time is",round(t2-t1))




        



