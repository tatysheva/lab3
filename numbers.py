print('Enter 4 numbers: ')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))
num4 = float(input('Enter fourth number: '))

sum1 = num1 + num2
sum2 = num3 + num4

print("first + second = {0}" .format(sum1))
print("third + fourth = {0}" .format(sum2))
print("first sum + second sum = %.2f" % (sum1 / sum2))