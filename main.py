# Brenden Brahier
def menu_selection():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")


def encode_pass(password):
    new_pass = ""
    for char in password:
        num = int(char)
        num = num + 3
        new_pass += str(num)
    return new_pass

if __name__ == '__main__':
    user_input = 0
    while True:
        menu_selection()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = (input("Please enter your password to encode: "))
            encode_pass(password)
        if user_input == 3:
            break