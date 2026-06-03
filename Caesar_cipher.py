def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


choice = input("Encrypt or Decrypt (E/D): ").upper()

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == "E":
    print("Encrypted:", encrypt(message, shift))

elif choice == "D":
    print("Decrypted:", decrypt(message, shift))

else:
    print("Invalid Choice")