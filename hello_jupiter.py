import random;

def get_input(prompt):
    # 標準入力から整数値を取得する
    return int(input(prompt))

def get_random_number(min_value, max_value):
    # min_valueとmax_valueの間のランダムな整数を生成する
    return random.randint(min_value, max_value)

min_value = get_input("最小値を入力してください")
max_value = get_input("最大値を入力してください")

# 最小値が最大値より大きくないか確認
while min_value > max_value:
    if min_value > max_value:
        print("入力値が不正です。最小値が最大値より大きいです")
        min_value=get_input("最小値を入力してください")
        max_value = get_input("最大値を入力してください")

# 回答制限回数
inputLimitTimes=5
# 現在の回答回数カウント
currInputTime=1

target = get_random_number(min_value, max_value)

print(str(min_value)+"~"+str(max_value)+"の中から正解の数字を当ててください")

answer = int(input("1回目!"))

while(answer != target):
    if(currInputTime>inputLimitTimes):
        print("回答制限回数を超えました。残念でした！")
        break

    if(answer == target):
        print("あたりです！")
        break
    elif(answer > target):
        print("もっと小さいです！")
    else: 
        print("もっと大きいです")

    answer = int(input(str(currInputTime)+"回目！..."))
    currInputTime+=1

print("答えは..." + str(target))


