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


def decode_pass(password):
    decoded_pass = "".join(str(int(item)-3) for item in password)
    return decoded_pass


if __name__ == '__main__':
    user_input = 0
    while True:
        menu_selection()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = (input("Please enter your password to encode: "))
            encoded_pw = encode_pass(password)
        elif user_input == 2:
            print(f'The encoded password is {encoded_pw}, and the original password is {decode_pass(encoded_pw)}')
        if user_input == 3:
            break
