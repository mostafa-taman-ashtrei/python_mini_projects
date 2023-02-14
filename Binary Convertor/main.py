translating, invalid = True, False

while translating:
    if invalid:
        print("Invalid option please choose a valid one!")
        print("-------------------------------------------------------------")

    print("(1) Choose b2t to convert binary code into text")
    print("-------------------------------------------------------------")
    print("(2) Choose t2b to convert text into binary code")
    print("-------------------------------------------------------------")
    print("(3) Choose q to quit")

    user_choice = input().lower()

    if user_choice == 't2b':
        text_messge = input("Enter the text you want to convert: ")
        binary_code = " ".join(format(ord(char), 'b')
                               for char in text_messge)
        print(f"Binary Code ---> {binary_code}")
        print("-------------------------------------------------------------")

    elif user_choice == 'b2t':
        binary_code = input("Enter the binary code you want to convert: ")

        text_messge = " ".join(chr(int(char, 2))
                               for char in binary_code.split(" "))

        print(f"Text ---> {text_messge}")
        print("-------------------------------------------------------------")

    elif user_choice == 'q':
        translating = False

    else:
        invalid = True
