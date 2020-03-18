#c = (x-n)%26

def encripted(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) #ASCII values of all upper_case values start from 65
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) #ASCII values of all lower_case values start from 97

    return cipher

text = input("enter the text: ")
s = int(input("enter the shift key"))
print("the original string is : ", text)
print("the encripted message is :",encripted(text,s))