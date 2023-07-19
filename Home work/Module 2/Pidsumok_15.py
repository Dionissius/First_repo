
wait_for_number = True

enter = input('Enter num: ')
result = float(enter)

while wait_for_number:

    while True:
        operation = input('Operation: ')

        if operation == '=':
            wait_for_number = False
            print(f'result is {result}')
            break

        if (operation != '+') and (operation != '-') and (operation != '*') and (operation != '/'):
            print(f"{operation} is not '+' or '-' or '/' or '*'. Try again")

        if operation == '+':
            while True:
                enter2 = input('Enter num: ')

                try:
                    result = result + float(enter2)
                except ValueError:
                    print(f"{enter2} is not a number. Try again.")
                else:
                    break


        if operation == '-':
            while True:
                enter2 = input('Enter num: ')

                try:
                    result = result - float(enter2)
                except ValueError:
                    print(f"{enter2} is not a number. Try again.")
                else:
                    break

        if operation == '*':
            while True:
                enter2 = input('Enter num: ')

                try:
                    result = result * float(enter2)
                except ValueError:
                    print(f"{enter2} is not a number. Try again.")
                else:
                    break

        if operation == '/':
            while True:
                enter2 = input('Enter num: ')

                try:
                    result = result / float(enter2)
                except ValueError:
                    print(f"{enter2} is not a number. Try again.")
                else:
                    break

