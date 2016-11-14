traductions = {
    "dog" : "chien",
    "cat" : "chat",
    "car" : "voiture"
}


print ("Hello, welcome to the quizz")

for question in traductions:
    user_answer = input (question + " est : " )
    real_answer = traductions [question]

    if user_answer == real_answer :
        print ("correct")
    else :
        print ("faux")






