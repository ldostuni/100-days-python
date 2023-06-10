def caesar(message, shift_num, choice):
    alphabet = "abcdefghijklmnopqrstuvz"
    new_message = ""
    for i in range(0, len(message)):
        index = alphabet.find(message[i])
        if index == -1:
            new_message += message[i]
        else:
            if choice == 'encode':
                new_message += alphabet[(index + shift_num) % len(alphabet)]
            else:
                new_message += alphabet[(index - shift_num) % len(alphabet)]
    return new_message

cont = "yes"
while cont == "yes":
    choice = input("type 'encode' or 'decode': ").lower()
    message = input("Type your message: ").lower()
    shift_num = int(input("type your shift number: "))

    new_message = caesar(message, shift_num, choice)
    print("Here's the new message:", new_message)

    cont = input("Do you want to continue? Yes or no: ").lower()