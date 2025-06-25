def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt? (e/d): ")

if choice.lower() == 'e':
    print("Encrypted:", encrypt(message, shift))
else:
    print("Decrypted:", decrypt(message, shift))
