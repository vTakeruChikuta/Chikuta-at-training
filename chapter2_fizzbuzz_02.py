a = input('自然数を入力するのだ')

if str.isdecimal(a) == False:
    print('自然数が入力されていないのだ') # whileで正しく入力されるまで繰り返すのが一番だががっつり別課題なので

a = int(a)
if (a % 3) == 0 and (a % 5) == 0:
    print('FizzBuzz')
elif (a % 3) == 0:
    print('Fizz')
elif (a % 5) == 0:
    print('Buzz')
else:
    print('5でも3でも割り切れないぞ！')
