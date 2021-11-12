#import the necessary libraries such as the os library for storing the outcomes and the random library for getting a random word
import os
import random

#this is the spacer variable used to give the output better aesthetic
spacer='#'*60

#this variable houses the maximum number of wrong guess attempts the game allows 
amount_of_tries=10

#this function generates a randomly selected word for the player to guess
def get_word():
    list_of_words=["hello","glass","green","infinitesimal","obscure","hostility"]
    return random.choice(list_of_words)

#this function gets a hint for the randomly selected word
def get_hint(word):
    hint={"hello":"commonly used as a greeting irrespective of time of day",
          "glass":"a hard and sharp substance made from sand",
          "green":"color usually associated with money",
          "infinitesimal":"means something extremely small",
          "obscure":"means something hidden or unclear",
          "hostility":"a show of obvious disdain or dislike for someone or something"}
    return "hint: "+hint[word]

#this ensures that the players guess is an alphabet
def error_checker(stri,word):
    if stri.isalpha():
        return True
    else:
        return False

#this function is in charge of logging all wins and losses in a file 
def file_record(status):
    status='\n'+status
    file=open(os.path.expanduser('~')+'/Desktop/rwgp.txt','a+')
    file.write(status)
    file.close()

#this is incharge of the initial display of information that players should note before playing
def greet_rules():
    print("\t\t\tWelcome to Ryan's word game project")
    print("\t\t\t***********************************")
    print("\nPlease read the following information before starting:")
    print("\nYou will be prompted to enter a letter or an entire word which will continue until you guess all the letters in \nthe randomly selected word, guess the actual complete word or you exhaust all of your tries.\nYour wins and losses will be saved in a file for further review called rgwp.txt.\nThank you for playing and have a nice time :).\n\nclick enter to continue")
    input()

#this houses the main logic behind how the game works    
def game_logic(guess_word,amount):
        
        ansa="_"*len(guess_word)
        copy=guess_word
        set_word=str(set(guess_word))
        count=0
        return_val="WIN"
        game_over=False
        
        while not game_over:
            print(spacer)
            print(get_hint(copy))
            
            letter=input("enter a letter, group of letters or word:")
            
            if error_checker(letter,copy):
                if (letter in guess_word or letter in set_word) and len(letter)<len(copy):
                     print('right')
                    
                     for l in letter:
                        while guess_word.find(l)!=-1:
                            index=guess_word.index(l)
                            guess_word=guess_word.replace(l," ",1)
                            set_word=set_word.replace(l," ",1)
                            ansa=ansa[:index]+l+ansa[index+1:]
                    
                     print("progress: "+ansa)
                    
                     if ansa==copy:
                            print(spacer)
                            print("you won yaay")
                            print("the word was ",ansa)
                            game_over=True
                        
                elif letter==copy:
                    print(spacer)
                    print("you won yaay")
                    print("the word was ",copy)
                    game_over=True
                        
                else:
                    print('wrong')
                    count+=1
                    print('you have ',amount-count,' tries left')
                    if count==amount:
                        print(spacer)
                        print("you failed u have ",amount-count," tries left the word was",copy)
                        return_val="LOST"
                        game_over=True
            else:
                print('An error occured due to bad input.Please use apporiate input')
                count+=1
                print('you have ',amount-count,' tries left')
                if count==amount:
                    print("you failed u have ",amount-count," tries left. the word was ",copy)
                    return_val="LOST"
                    game_over=True
        
        return return_val

#this is the main game functions that combines the functionaity of all the other functions together
def game(guess_word,amount):
    greet_rules()
    file_record(game_logic(guess_word,amount))
    
#this function call acts as the entry point for our program  
game(get_word(),amount_of_tries)            
