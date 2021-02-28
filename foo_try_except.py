#foo_try_except.py

try:
    number = float(input("enter non-zero real number divisor: "))
    result = 100.0/number
    print()
    print("Result is: ", result)
except:
    print("Except: Invalid value is entered")
else:
    ##
    print("Else: This message will be displayed if there is no crash!")
finally:
    ##
    print('finally: This line will be displayed always regardless error or no. try statement(try except else finally)')

##always printed
print("This message will be displayed always, continue!")