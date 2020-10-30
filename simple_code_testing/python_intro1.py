name = input('Enter your name  please: ')
num1 = 0
num2 = 0
def hi(name):
    print(f'Hi there {name}!')
    print('How are you?')
    print(f'{name}, you\'ll need to enter two numbers')

def two_numbers(num1, num2):
    num1 = int(input('First number please: '))
    num2 = int(input('Second number please: '))
    if num1 != num2:
        return print(f'{num1} is not equal to {num2}')
    if num1 > num2:
        return print(num1 +'is greater than' + num2)
    

hi(name)
two_numbers(num1, num2)
