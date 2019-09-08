import random
def hangman(word):
    word_list = list(word)
    hyouji = "_" * len(word)
    hyouji_list = list(hyouji)
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]

    while len(stages)-1 >= wrong:
        print(hyouji)
        answer = input("1文字入力してください")
        if answer in word_list:
            answer_number = word.index(answer)
            hyouji_list[answer_number] = word_list[answer_number]
            word_list[answer_number] ="$"
            hyouji ="".join(hyouji_list)
            if hyouji == word:
                print("ゲームクリアおめでとう！")
                break
        else:
            wrong += 1
            print("\n".join(stages[0:wrong-1]))

animal =["cat","dog","fox","lion","tiger"]
a = random.randint(0,len(animal)-1)
hangman(animal[a])