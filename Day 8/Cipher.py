def cipher(word, todo, c_num):
    cipher_text = ""
    if todo == "decode":
        c_num *= -1
    for i in word:
            char = i
            if i.islower():
                cipher_text += chr((ord(char) - 97 + c_num) % 26 + 97)
            elif i.isupper():
                cipher_text += chr((ord(char) - 65 + c_num) % 26 + 65)
            elif i.isdigit():
                cipher_text += chr((ord(char) - 48 + c_num) % 10 + 48)
            else:
                cipher_text += char
    return cipher_text
