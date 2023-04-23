import json
import random
import time
import os

point = 0

def main():
    init()
    json_file = read()
    length = len(json_file["question"])
    global point

    #初期処理
    question_random = rand(0,length-1) #問題と正解を選ぶ
    print(str(json_file["question"][question_random][0])+"のポート番号は？")

    #選択肢の生成
    choice_list = []
    choice_list.append(json_file["question"][question_random])
    while len(choice_list) != 4:
        tmp = json_file["question"][rand(0,length-1)]
        if tmp not in choice_list:
            choice_list.append(tmp)
    random.shuffle(choice_list)
    for i in range(1,5):
        print(str(i) + ". " + str(choice_list[i-1][1]),end="     ")
    print()

    #入力受付
    answer_input = int(input("あなたの解答："))
    if answer_input < 0 or 4 < answer_input:
        print("不正な入力です。")
        fin()

    while answer_input != 0:
        gap()
        if choice_list[answer_input-1][1] == json_file["question"][question_random][1]:
            print("正解！！")
            point += 1
        else:
            print("不正解…………")
            print(str(json_file["question"][question_random][0])+"のポート番号は"+str(json_file["question"][question_random][1])+"です。")
        
        print()
        time.sleep(0.5)
        print("次へ行くにはエンターを押して下さい。")
        tmp2 = input()
        if tmp2 != "":
            print("不正な入力です。")
            fin()
        os.system("clear")
        
        #初期処理
        question_random = rand(0,length-1) #問題と正解を選ぶ
        print(str(json_file["question"][question_random][0])+"のポート番号は？")

        #選択肢の生成
        choice_list = []
        choice_list.append(json_file["question"][question_random])
        while len(choice_list) != 4:
            tmp = json_file["question"][rand(0,length-1)]
            if tmp not in choice_list:
                choice_list.append(tmp)
        random.shuffle(choice_list)
        for i in range(1,5):
            print(str(i) + ". " + str(choice_list[i-1][1]),end="     ")
        print()

        #入力受付
        answer_input = int(input("あなたの解答："))
        if answer_input < 0 or 4 < answer_input:
            print("不正な入力です。")
            fin()
        
    fin()

def init():
    os.system("clear")
    print("ウェルノウンポートクイズを始めるよ")
    print("半角数字1～4で解答して下さい。0を入力すると終了します。")
    time.sleep(0.5)
    print()
    return

def read():
    with open("data.json") as f:
        return json.load(f)

def rand(x,y):
    return random.randrange(x,y)

def gap():
    print()
    s = ""
    for i in range(8):
        s += "**"
        time.sleep(0.2)
        print("\r"+s,end="")
    print("\n")

def fin():
    global point
    time.sleep(0.5)
    print("終了します。")
    print("あなたの正解数は"+str(point)+"回でした！")
    exit()

if __name__ == "__main__":
    main()