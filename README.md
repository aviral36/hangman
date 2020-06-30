# Hangman
 A hangman game built on python3.
 <br><br>
 The code was not built by me. It was built by my friend pursuing MBBS. Despite belonging to a non-coding background, my friend worked incredibly hard to build this amazing code. <br><br>
 Apologies, but I will not accept any pull requests/ amendments to this code.<br> I wish to keep it just the way it was meant to be, to respect the hard work of its creator.
 
 ### Setup
 
 Download the repository to your computer.
 Extract the files and run game.py
 <br><br>
 NOTE: You need to have Python3 installed on your computer for the script to work.
 
 External libraries used: None
 
 ### File Descriptions
 
 /meta: stores six different colored hangman logos, which can be used in a tkinter interface, in case you wish to build a GUI.
 <br><br>
 english_words.txt: contains nearly a thousand english words, non-categorised. Words less than length 4 have been removed from consideration as guessing a small word is tough. Further, for a better guessing experience, the number of blanks inserted in a word of length l cannot exceed int(l/2). This means for a 9 letter word "beautiful", no more than 4 blanks will be inserted by the code.
 <br><br>
 game.py: a python3 file containing all the game functions. You need to only run this file to play the game.
 <br><br>
 highscores.txt: stores the high scores in a simple text file. Does not associate player name with highscore.
 
 ### Developments
 
 As the code has not been changed, it leaves a major scope for further developments. 
 <br>
Replacing the english_words.txt file with a countries/cities file can make this game more interesting. All we need to do is copy/paste a file containing all the words you want *newline separated* and replace the file in f=open('file','r') with your filename.
<br><br>
Another development can introduce a GUI to this game. This will require you to use PIL/tkinter libraries on python, or you can download pygame module for added functionality.
<br>
 
 
