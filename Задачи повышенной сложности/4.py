k = int(input("add value for k: "))
num_par = 1
n = 1
posl = 10
p = 10
for j in range(89):
    if k == n or k == n+1:
        print('\nНомер пары цифр, в которую входит k-я цифра: ', num_par)
        print('Двузначное число, образованное парой цифр, в которую входит k-я цифра: ', p)
        if k == n+1: print('k-я цифра: ', p%10)
        else: print('k-я цифра: ', p//10)
    p+=1
    posl = posl * 100 + p
    num_par+=1
    n+=2
print('\nПоследовательность цифр: ', posl)
