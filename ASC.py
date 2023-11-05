import math
def encrypt(key, message):
    ciphertext = [''] * key
    for column in range(key):
        index = column
        while index < len(message):
            ciphertext[column] += message[index]
            index += key
    return ''.join(ciphertext)
def decrypt(key, message):
    nrows = key
    ncols = math.ceil(len(message) / key)
    empty_positions = nrows * ncols - len(message)
    plaintext = [''] * ncols
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if column == ncols or (column == ncols - 1 and row >= nrows - empty_positions):
            column = 0
            row += 1
    return ''.join(plaintext)
message = input("Enter the message: ")
key = int(input("Enter the key: "))
loop = int(input("Enter the number of the times to be repeated: "))
for i in range(loop):
    ciphertext = encrypt(key, message)
print(f'Ciphertext: {ciphertext}<end>')
for i in range(loop):
    plaintext = decrypt(key, ciphertext)
print(f'Plaintext: {plaintext}')