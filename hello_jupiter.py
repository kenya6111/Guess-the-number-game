import random;

def get_input(prompt):
    # 標準入力から整数値を取得する
    return int(input(prompt))

def get_random_number(min_value, max_value):
    # min_valueとmax_valueの間のランダムな整数を生成する
    return random.randint(min_value, max_value)

def guess_number_game():
    min_value = get_input("最小値を入力してください")
    max_value = get_input("最大値を入力してください")

    # 最小値が最大値より大きくないか確認
    while min_value > max_value:
        if min_value > max_value:
            print("入力値が不正です。最小値が最大値より大きいです")
            min_value = get_input("最小値を入力してください")
            max_value = get_input("最大値を入力してください")

    # 答えを取得
    target = get_random_number(min_value, max_value)

    print(f"{min_value}~{max_value}の中から正解の数字を当ててください")

    # 回答制限回数
    input_limit_times=5
    # 現在の回答回数カウント
    curr_input_time=1

    while curr_input_time <= input_limit_times:

        answer = get_input(f"{curr_input_time}回目！数字を当ててください: ")

        if answer == target :
            print("あたりです！")
            break
        elif answer > target :
            print("もっと小さいです!")
        else: 
            print("もっと大きいです!")

        curr_input_time += 1

        if(curr_input_time > input_limit_times):
            print("回答制限回数を超えました。残念でした！")

    print("答えは..." + str(target))

if __name__ == "__main__":
    guess_number_game()
