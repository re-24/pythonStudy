import random

win = 0
draw = 0
count = 0;
while 1:

    print("じゃんけん" + str(count) + "回目")
    print("> 0:グー、1:チョキ、2:パー")

    com = random.randint(0,2)
    you = int(input("あなたの手は？"))
    if you == 9:
        break

    count += 1    # dddd

    print("コンピュータの手=" + str(com))
    if com == 0:
        if you == 2:
            print("勝ち")
            win += 1
        elif you == 1:
            print("負け")
        elif you == 0:
            print("あいこ")
            draw += 1
    elif com == 1:
        if you == 0:
            print("勝ち")
            win += 1
        elif you == 2:
            print("負け")
        elif you == 1:
            print("あいこ")
            draw += 1
    elif com == 2:
        if you == 1:
            print("勝ち")
            win += 1
        elif you == 0:
            print("負け")
        elif you == 2:
            print("あいこ")
            draw += 1



print("結果=" + str(count) + "戦" + str(win) + "勝" + str(draw) + "引き分け")
