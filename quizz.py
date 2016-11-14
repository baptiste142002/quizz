

def get_word(type_mot):

    print("welcome to the quizz")
    name = input("Choisissez votre "+type_mot+" ? ")
    message = "Le mot choisis est: " + name
    print(message)


def get_words () :
    print ("Bienvenue dans le quizz sur le cours")
    get_word ("fruit")
    get_word ("couleur")
    get_word ("forme")

get_word("mot")
get_words ()

