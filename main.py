from math import *

num1 = input("Enter first number: ")
num1_int = int(num1)
if num1.isdigit():
    print('''
    1 mean + operation
    2 mean - operation
    3 mean * operation
    4 mean / operation
    5 mean ^ operation
    6 mean % operation
    ''')

    operation_num_str = input("Enter operation number: ")
    operation_num_int = int(operation_num_str)
    if operation_num_int == 1 or operation_num_int == 2 or operation_num_int == 3 or operation_num_int == 4 or operation_num_int == 5 or operation_num_int == 6:
        num2 = input("Enter second number: ")
        num2_int = int(num2)
        if num2.isdigit():
            if operation_num_int == 1 :
                sum_num_int = num1_int + num2_int
                sum_num_str = str(sum_num_int)
                print(num1 + " + " + num2 + " = " + sum_num_str)
                result = sum_num_int
            elif operation_num_int == 2:
                minus_num_int = num1_int - num2_int
                minus_num_str = str(minus_num_int)
                print(num1 + " - " + num2 + " = " + minus_num_str)
                result = minus_num_int
            elif operation_num_int == 3:
                mul_num_int = num1_int * num2_int
                mul_num_str = str(mul_num_int)
                print(num1 + " * " + num2 + " = " + mul_num_str)
                result = mul_num_int
            elif operation_num_int == 4:
                division_num_int = num1_int / num2_int
                division_num_str = str(division_num_int)
                print(num1 + " / " + num2 + " = " + division_num_str)
                result = division_num_int
            elif operation_num_int == 5:
                power_num_int = num1_int ** num2_int
                power_num_str = str(power_num_int)
                print(num1 + " ** " + num2 + " = " + power_num_str)
                result = power_num_int
            elif operation_num_int == 6:
                mod_num_int = num1_int % num2_int
                mod_num_str = str(mod_num_int)
                print(num1 + " % " + num2 + " = " + mod_num_str)
                result = mod_num_int
            else:
                print("NO operation")
            if type(result) is int or  type(result) is float:
                print('''
                   1 mean round
                   2 mean ceil
                   3 mean floor
                   ''')
                num_rounding = input("Enter a number from 1 to 3: ")
                num_rounding = int(num_rounding)
                if num_rounding == 1:
                    print(round(result))
                elif num_rounding == 2:
                    print(ceil(result))
                elif num_rounding == 3:
                    print(floor(result))

             



