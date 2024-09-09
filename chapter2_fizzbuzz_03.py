a = ''  # aを宣言
n = 0  # ループようにnを用意

while n != 1:  # 判定はifに任せて、満たしたときにn+1でループ終了
    a = input('数字を入力しなさい')

    if a == '':  # 入力がないと入力しなおし
        print('ちゃんと入力しなさい')

        continue

    if str.isdecimal(a) == False:  # 数が入っていないと入力しなおし
        print('数字しか入れてはいけません')

        continue

    a = int(a)  # intに変換
    if (a % 3) == 0 and (a % 5) == 0:  # 両方で割る判定
        print('FizzBuzz')
        n = n + 1

    elif (a % 3) == 0:  # 3で割る判定
        print('Fizz')
        n = n + 1

    elif (a % 5) == 0:  # 5で割る判定
        print('Buzz')
        n = n + 1

    elif not (a % 3 == 0 or a % 5 == 0):  # 割り切れないときにループ最初に戻る
        print('3か5で割り切れる数を入力しなさい')
