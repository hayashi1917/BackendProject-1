
import random
while True:
    print("最大値を入力:")
    max = int(input())
    print("最小値を入力:")
    min = int(input())
    if max >= min:
        break
    else:
        print("最大値は最小値より大きくしてください")

randomNumber = random.randint(min, max)

while True:
    print("数値を入力:")
    inputNumber = int(input())
    if inputNumber == randomNumber:
        print("正解")
        break
    else:
        print("不正解")

