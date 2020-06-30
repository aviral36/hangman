import tkinter as tk
from PIL import ImageTk, Image
import random

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


x = 0
score = 0
play = 1
game = tk.Tk()

game.title("Hangman")
game.geometry("500x500")

image_no = random.randint(1,5)
path = "meta/Picture" + str(image_no) + ".png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(game, image = img)
panel.pack(side = "top")
spacer0 = tk.Label(game, text = "\n")
spacer0.pack()

file = open('highscore.txt', 'r+')              #opens a file containing highscores
highscore = file.read()    #make a list of all words
if highscore == '':                             #if there are no scores, put highscore = 0
    hs = tk.Label(game, text = "Highscore is 0")
    hs.pack()
else:
    s =  "Highscore is " + str(highscore)
    hs = tk.Label(game, text = s)
    hs.pack()

t = tk.Text(game, state = 'disabled', height = 5)
t.configure(state='normal')
t.insert('end', 'Welcome to hangman. Prepare to be hanged')
t.configure(state='disabled')
t.pack()
spacer = tk.Label(game, text = "\n")
spacer.pack()
end_button = tk.Button(game, text = 'Quit', command = game.destroy, width = 20)
end_button.pack()
game.mainloop()
