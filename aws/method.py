def converter(roman):
    result=""
    m_ler = int(roman) // 1000
    result = result + m_ler*"M"
    kalan = int(roman) % 1000
    cm_ler = kalan // 900
    result = result + cm_ler*"CM"
    kalan =  kalan % 900
    d_ler = kalan // 500
    result = result + d_ler*"D"
    kalan =  kalan % 500
    cd_ler = kalan // 400
    result = result + cd_ler*"CD"
    kalan =  kalan % 400
    c_ler = kalan // 100
    result = result + c_ler*"C"
    kalan =  kalan % 100
    xc_ler = kalan // 90
    result = result + xc_ler*"XC"
    kalan =  kalan % 90
    l_ler = kalan // 50
    result = result + l_ler*"L"
    kalan =  kalan % 50
    xl_ler = kalan // 40
    result = result + xl_ler*"XL"
    kalan =  kalan % 40
    x_ler = kalan // 10
    result = result + x_ler*"X"
    kalan =  kalan % 10
    ix_ler = kalan // 9
    result = result + ix_ler*"IX"
    kalan =  kalan % 9
    v_ler = kalan // 5
    result = result + v_ler*"V"
    kalan =  kalan % 5
    iv_ler = kalan // 4
    result = result + iv_ler*"IV"
    kalan =  kalan % 4
    i_ler = kalan // 1
    result = result + i_ler*"I"

    print(result) 
    

converter(3999)

print("aaaaaaaaaaaaaaaaaa")

def convert(decimal_num):
    # set the dictionary for roman numerals
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # initialize the result variable
    num_to_roman = ''
    # loop the roman numerals, calculate for each symbol and add to the result
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman

# flag to show warning to the user, default is False.
is_invalid = False

# start endless loop to get user input continuously
while True:
    # info text to be shown to the user
    info = """
###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : """

    # get the user input after showing info text.
    # if is_invalid set to True then show additional warning to the user
    # pass the input the alphanum variable after stripping white space characters
    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    # if the input is not decimal number
    if not alphanum.isdecimal():
        # then check, if it is the "exit" keyword
        if alphanum.lower() == 'exit':
            # if it is "exit", then say goodbye and terminate the program
            print('\nExiting the program... Good Bye')
            break
        # if it is a strint other than "exit"
        else:
            # then set to invalid flag to True to show warning and continue with next cycle
            is_invalid = True
            continue
    # convert the given string to the integer
    number = int(alphanum)
    # if the number is between 1 and 3999, inclusively
    if 0 < number < 4000:
        # then convert to roman numerals and print out the user
        print(
            f'\nRoman numerals representation of decimal number "{alphanum}"" is equal to {convert(number)}')
        # and set invalid flag to the False, it might be set the True in previous cycle
        is_invalid = False
    # if the number is out of bounds
    else:
        # then set to invalid flag to True to show warning
        is_invalid = True