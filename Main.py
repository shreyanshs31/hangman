'''
 * Created By: Shreyansh Shukla
 * Date: 02-07-2023
 * Project Name: Hangman Game
 *
 '''


from random import randint


def main():
    #Display all the rules
    print("1. There will be 5 lives")
    print("2. For every wrong letter you lose one life and the person gets closer to being hanged")
    print("3. All the words will be more than 5 letters")
    print("4. Only vowels in the word will be displaied")
    print("5. Enter one letter at a time")

    #take name form the user
    name = input("Enter your name: ")

    #take a random word form the words.txt file
    #see if its length is greater than 5 letters
    rword = ""
    with open("words.txt", "r") as file:
        word = file.readlines()
        rline = randint(0, 854)
        while(True):
            if len(word[rline][:-1]) > 5:
                break
            else:
                rline = randint(0,854)
        #Used string slicing to remove \n attached to the word        
        rword = word[rline][:-1] 
    tword = ""
    t = list(rword)
    vowel = ["a", "e", "i", "o", "u"]
    for i in range(len(t)):
        if t[i] not in vowel:
            #if the letter not a vowel make it _ to hide the letter
            t[i] = "_" 
    tword = "".join(t)

    #start the game
    chance = 5
    display(chance)
    while chance > 0:
        print(tword)
        eletter = input("Enter the letter: ")
        temp = list(rword)
        # if the letter is present in the word make it visible
        if eletter in rword:
            for i in range(len(rword)):
                if temp[i] == eletter:
                    t[i] = eletter
            tword = "".join(t)
            #if the word is complete then break the loop
            if tword == rword:
                break
        else:
            #if letter not present in the word life is reduced
            chance-=1
            display(chance)
            
    if chance == 0:
        print("You are hanged")
        print("Better luck next time")
    else:
        print("Contrulations {} you won".format(name))


#This function displayes the animation after every wrong attempt the person being hanged
def display(chance):
    if chance == 5:
        print(" _________")
        print(" |        ")
        print(" |        ")
        print(" |        ")
        print(" |        ")
        print(" ~~~~~~~~~~~")
    elif chance == 4:
        print(" _________")
        print(" |     |  ")
        print(" |        ")
        print(" |        ")
        print(" |        ")
        print(" ~~~~~~~~~~~")
    elif chance == 3:
        print(" _________")
        print(" |     |  ")
        print(" |    ( ) ")
        print(" |        ")
        print(" |        ")
        print(" ~~~~~~~~~~~")
    elif chance == 2:
        print(" _________")
        print(" |     |  ")
        print(" |    ( ) ")
        print(" |    -|- ")
        print(" |        ")
        print(" ~~~~~~~~~~~")
    elif chance == 1:
        print(" _________")
        print(" |     |  ")
        print(" |    ( ) ")
        print(" |    -|- ")
        print(" |    /   ")
        print(" ~~~~~~~~~~~")
    else:
        print(" _________")
        print(" |     |  ")
        print(" |    ( ) ")
        print(" |    -|- ")
        print(" |    / \ ")
        print(" ~~~~~~~~~~~")

#Calls the main function
if __name__ == "__main__":
    main()
