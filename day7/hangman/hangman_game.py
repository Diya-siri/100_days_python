import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        ''')
ascii=['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''','''
 +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''','''
 +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''','''
+---+
  |   |
  0   |
 /|   |
      |
      |
=========
''','''
+---+
  |   |
  0   |
  |   |
      |
      |
=========
''','''
+---+
  |   |
  0   |
      |
      |
      |
=========
''','''
+---+
  |   |
      |
      |
      |
      |
=========''']
print("Try to guess the name of a state in India!")
word_list=["karnataka","tamilnadu","andrapradesh","telangana","goa","sikkim","maharashtra","Gujarat","delhi","kerala","arunachalpradesh","punjab",
"jharkhand","haryana","rajasthan","mizoram","bihar","assam","tripura","manipur"]
chosen_word=(random.choice(word_list)).lower()
list=['-']
for i in range(0,len(chosen_word)-1):
    list.append('-')
end=False
lives=6
while not end:
    n=(input("Guess a letter:")).lower()
    if n in list:
        print("letter already guessed\n")
    for i in range(len(chosen_word)):
        m=chosen_word[i]
        if n==m:
            list[i]=m
    print(f"{ascii[6-lives]}")
    print(f"{' '.join(list)}")
    if n not in chosen_word:
        lives-=1
        print("the letter you chose is not in the word,you lose a life")
        if lives==0:
            end=True
            print("You lost")
            print(f"The solution is {chosen_word}.\n")
            break
        print(f"{ascii[6-lives]}")
    if "-" not in list:
        end=True
        print("Congrats!You won!")
        break
        

