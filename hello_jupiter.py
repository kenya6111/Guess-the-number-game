import sys;
import random;

min = int(input("最小値を入力してください"))
max = int(input("最大値を入力してください"))

while min > max:
    if min > max:
        max=int(input("最小値より大きい最大値を設定してください"))

target = int(random.uniform(min, max))

answer = int(input("数字を当ててください"))
inputLimitTimes=5
currInputTime=0
while(answer != target):
    if(currInputTime>inputLimitTimes):
        print("制限回数を超えました。残念でした！")
        break

    answer = int(input("残念！数字を当ててください"))
    currInputTime+=1
    
    

print("答えは..." + str(target))
