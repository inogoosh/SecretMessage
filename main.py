import random

def encoded_message(message, password):
    encoded = ""
    for char in message:
        encoded += chr(ord(char) + password)
    return encoded

def decoded_message(encoded_message, password):
    decoded = ""
    for char in encoded_message:
        decoded += chr(ord(char) - password)
    return decoded

def main():
    password = random.randint(161, 111411)
    while True:
        try:
            choice = int(input("Write 1 for Encoding and 2 for Decoding the Message, else enter any other key to exit: "))
        except ValueError:
            break

        if choice == 1:
            message = input("Enter your Secret message: ")
            result = encoded_message(message, password)
            print("Encoded Message:", result)
            print(f"Your Password is: {password}")
        elif choice == 2:
            encoded_input = input("Enter the Encoded text: ")
            try:
                password_input = int(input("Enter the password: "))
                print("Decoded Message:", decoded_message(encoded_input, password_input))
            except ValueError:
                print("Invalid password input.")
        else:
            break

if __name__ == "__main__":
    main()
