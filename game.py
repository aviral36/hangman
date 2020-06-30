import random
import tkinter

word = ["cruel", "alright", "stupid", "business", "delicate", "swift", "bandits"]
hints = ["cru_l", "alri__t", "stu__d", "b__iness", "del_c_te", "swi_t", "band__s"]

                                #I open a file containing 10k english words
f = open('english_words.txt', 'r')
words = f.read().splitlines()    #make a list of all words
f.close()                       #we don't need the file now, so close it

#making list with only words that are 4 or more letters
word_list = list()
for word in words:
    if len(word)>=4:
        word_list.append(word)


#generates random word from list of words

def getword():        
    number = random.randint(0, len(word_list)-1)    #churns out a random number between 0 and 10k
    word = word_list[number]                        #this number acts as an index to get a random word from list
    return word

#this function generates a word with blanks.     For eg:   "Beautiful" -> "Be_ut_ful
def blanks(word):
    length = len(word)
    max_no_of_blanks = int(length/2)             #a word can have max half the blanks its length. "Pretty" cannot have more than 3 blanks
    n_blanks = random.randint(1, max_no_of_blanks)      #decides the number of blanks the word will have
    indexes = random.sample(range(0, length-1), n_blanks)  #gives a list of indexes with numbers in range of 0 to length of word. n_blanks specifies how many numbers to generate.

    word_ = list(word)       # making a list of letter in the word. strings cannot be changed, but list can
    for idx in indexes:
        word_[idx] = '_'            #replaces the index with an underscore

    new_word = str()                #making a string back from list
    for i in word_:
        new_word = new_word + i

    return (new_word, n_blanks)


def hangman():
    x = 0
    score = 0
    play = 1
    file = open('highscore.txt', 'r+')              #opens a file containing highscores
    highscore = file.read()    #make a list of all words
    if highscore == '':                             #if there are no scores, put highscore = 0
        print("Highscore is 0")
    else:
        print("Highscore is ", highscore)
        highscore = int(highscore)
    while play:
        word = getword()
        blank_word, n_blanks = blanks(word)
        print("Guess the word -   ", blank_word, " (", n_blanks, " blanks)")
        answer = input("Enter your answer: ")
        if answer == word:
            score = score + 1
            print("Yay you win! He lives....." + "your score is " + str(score))
            print("The game was intentionally made simple, so that everyone can win - even you")
            a = input("Do you wish to play more? press [y] to play again and [n] to leave this cute piece of text alone!!  ")
            if a == "y":
                play = 1
            else:
                play = 0
                if highscore == '':                     #when player wants to quit game, we check for his score
                    file.seek(0)                        #seek(0) sends the cursor to the start of the file
                    file.write(str(score))              #updates the score if there was no previous highscore stored
                    file.close()
                else:
                    if highscore < score:               #if earlier highscore is less than current score
                        file.seek(0)
                        file.write(str(score))          #we update highscore with new score
                        file.close()    
                                                        #if highscore is already larger than current, we do nothing
                                                            
        else:
            print("You lost, He was hanged")
            print("The correct answer is " + word) 
            a = input("Do you want to try again? Press accordingly [y] or [n]  ")
            if a == "y":
                play = 1
            else:
                play = 0
                if highscore == '':                 #same lines of code again
                    file.seek(0)
                    file.write(str(score))
                    file.close()
                else:
                    if highscore < score:
                        file.seek(0)
                        file.write(str(score))
                        file.close()
                
hangman()
print("Game over")
