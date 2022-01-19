# Simple-Wordle-Python-Code
About less than a week into learning Python, I attempted to code Wordle (https://www.powerlanguage.co.uk/wordle/) from scratch. Code will be updated to be more user-friendly as my knowledge expands. 

How it works is that the code will generate a random 5 letter word from its list (wordle.txt), and you have to guess it. This is done so by inputting any 5-letter word, and the code will give you 6 tries to guess the word correctly. The hints given are:
1) Which letters are completely wrong
2) Which letters are correct, but in the wrong position
3) Which letters are correct and in the right position

If you exceed 6 tries, the code will stop running and print the correct answer for you. 

Any words that:
1) Do not start with caps
2) Are lesser or longer than 5 letters
3) Are not in the wordle.txt list

will be rejected by the program and not counted as an attempt. 
