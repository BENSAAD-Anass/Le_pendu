import pandas as pd
import random


#uploiding the word list
wordlist = pd.read_csv('liste_francais.txt', header = None)

#word selection function
def word_selection(df):
    range_df = df.shape[0]
    random_number = random.randint(0, range_df)
    selected_word = df.iat[random_number,0]
    while len(selected_word)<6 :
        random_number = random.randint(0, range_df)
        selected_word = df.iat[random_number,0]
        break
    return selected_word

#function to split the word selected to letters
def word_splitter(wd):
    wd_list=list(wd)
    return wd_list

#check the letter given by user against the word chosen
def letter_checker(letter, wd_letters):
    s=[]
    for i in range(len(wd_letters)):
        if letter == wd_letters[i] :
            s.append(1)
        else :
            s.append(0)
    return s

def word_with_hidden_letters(letter,liste_bo,word_with_hidden):
    if len(word_with_hidden) != len(liste_bo):
        word_with_hidden=["_"]*len(liste_bo)
    else :
        for i in range(0, len(word_with_hidden)):
            if liste_bo[i] == 1 :
                word_with_hidden[i]=letter
    return word_with_hidden


word=str(word_selection(wordlist))
print(word)
print("Le nombre de lettre dans le mot est : ", len(word))
counter = 7
list_word=[]

while counter > 0 :
    x=input("tape a letter : ")
    list_boo=[]
    list_boo=letter_checker(x,word_splitter(word))
    list_word=word_with_hidden_letters(x,list_boo,list_word)
    print(list_word)
    if 1 not in list_boo :
        counter = (counter -1)
    if "_" not in list_word :
        break
    print(counter)

if "_" not in list_word :
    print ("you win")
else :
    print("you lost")
