import random


my_file = open("wordle.txt", 'r')
wordle = my_file.read()
wordle_list = wordle.split(",")
my_file.close()

answer = str(random.choice(wordle_list))
answer_list=list(answer)
c = []
attempts = 0
smol = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


while attempts < 7:
    attempt = str(input(f'Guess a 5 letter word! {6-attempts} guesses only :^) ' + '\n'+'All letters start with caps! Not the bald Caps from LEC KEKW' + '\n' + '\n'))
    
    if len(attempt) != 5:
        print('This is not 5 letters you bonobo!')
        continue
    elif attempt[0] in smol:
        print ('Starts with caps sir... ')
        continue
    elif attempt not in wordle_list:
        print ('Not a valid word!')
        continue
    
    if attempt == answer:
            print(f'Congratulations! {attempt} is correct!')
            break
    else:
            attempts+=1
            print('You have '+ str(6-attempts) + ' attempt(s) ' + 'left. ')
            for word in range(len(answer)):
                if attempt[word] == answer[word]:
                    print(f'{attempt[word]} is correct')
                if attempt[word] != answer[word]:
                    c.append(attempt[word])
                    c=list(set(c))
                
            for word in c:    
                if word in answer_list:
                    print(f'{word} is correct but in the wrong spot')
                    
                if word not in answer_list:
                    print(f'{word} is wrong')
            list.clear(c)
                    
                
    if attempts > 5:
            print()
            print(f'You ran out of guesses. The correct word is {answer} ')
            break    
          
weweewe
        
        
    
   

    
                


        
            

    
