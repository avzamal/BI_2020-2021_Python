"""
enter the 2 numbers and operation symbol and
check first_num and second_num is numbers
"""
first_num = input()
if not first_num.isnumeric():
    print('First number is not a number')
else:
    first_num = int(first_num)
action = input()
second_num = input()
if not second_num.isnumeric():
    print('Second number is not a number')
else:
    second_num = int(second_num)
# check the operation symbol and print the result
if action == '-':
    print(first_num - second_num)
elif action == '+':
    print(first_num + second_num)
elif action == '*':
    print(first_num * second_num)
elif action == '/':
    # check second_num is not zero
    if second_num != 0:
        print(first_num / second_num)
    else:
        print('Division by zero')
else:
    print('Try another operation')
