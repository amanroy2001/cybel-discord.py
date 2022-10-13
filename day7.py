#GAme Name Hangman:
import random
def main():
    word_list=["aman","ashima","annu","shivam","shiddhant"]
    chosen_word=random.choice(word_list)
    lives=10
    #print(lives)
    lst = []
    lst.extend(chosen_word)
    #print(lst)
    #print(lst[1])
    #print(lst)
    while lives!=0:
        guess=input("Guess the word ")
        guess=guess.lower()
        for i in lst:
            if lst[i]==guess:
                lst[i].pop()
            else:
                lives-=1


main()

