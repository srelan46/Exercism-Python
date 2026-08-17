"Encode and decode text based on Atbash cipher"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"
def encode(plain_text):
    "encode text"
    result = ""
    for text in plain_text.lower():
        if text.isalpha():
            result+=CIPHER[ord(text)-ord('a')]
        elif text.isdigit():
            result += text
    groups = []

    for index in range(0, len(result), 5):
        groups.append(result[index:index + 5])

    return " ".join(groups)

def decode(ciphered_text):
    "decode text"
    result = ""
    for text in ciphered_text.lower():
        if text.isalpha():
            result+=CIPHER[ord(text)-ord('a')]
        elif text.isdigit():
            result += text
    return result
