import struct
def left_rotate(x, c):
    return (x << c) | (x >> (32 - c))
def F(x, y, z):
    return (x & y) | ((~x) & z)
def G(x, y, z):
    return (x & z) | (y & (~z))
def H(x, y, z):
    return x ^ y ^ z
def I(x, y, z):
    return y ^ (x | (~z))
def md5(data):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    K = [0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE,
         0xF57C0FAF, 0x4787C62A, 0xA8304613, 0xFD469501,
         0x698098D8, 0x8B44F7AF, 0xFFFF5BB1, 0x895CD7BE,
         0x6B901122, 0xFD987193, 0xA679438E, 0x49B40821,
         0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA,
         0xD62F105D, 0x02441453, 0xD8A1E681, 0xE7D3FBC8,
         0x21E1CDE6, 0xC33707D6, 0xF4D50D87, 0x455A14ED,
         0xA9E3E905, 0xFCEFA3F8, 0x676F02D9, 0x8D2A4C8A,
         0xFFFA3942, 0x8771F681, 0x6D9D6122, 0xFDE5380C,
         0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70,
         0x289B7EC6, 0xEAA127FA, 0xD4EF3085, 0x04881D05,
         0xD9D4D039, 0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665,
         0xF4292244, 0x432AFF97, 0xAB9423A7, 0xFC93A039,
         0x655B59C3, 0x8F0CCC92, 0xFFEFF47D, 0x85845DD1,
         0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1,
         0xF7537E82, 0xBD3AF235, 0x2AD7D2BB, 0xEB86D391]
    bit_len = len(data) * 8
    data += b'\x80'
    while (len(data) + 8) % 64 != 0:
        data += b'\x00'
    data += struct.pack('<Q', bit_len)
    for i in range(0, len(data), 64):
        chunk = data[i:i + 64]
        M = struct.unpack('<16I', chunk)
        AA, BB, CC, DD = A, B, C, D
        for j in range(16):
            A = B + left_rotate((A + F(B, C, D) + M[j] + K[j]), 7)
            A, B, C, D = D, A, B, C
        for j in range(16):
            k = (1 + 5 * j) % 16
            A = B + left_rotate((A + G(B, C, D) + M[k] + K[j + 16]), 12)
            A, B, C, D = D, A, B, C
        for j in range(16):
            k = (5 + 3 * j) % 16
            A = B + left_rotate((A + H(B, C, D) + M[k] + K[j + 32]), 17)
            A, B, C, D = D, A, B, C
        for j in range(16):
            k = (7 * j) % 16
            A = B + left_rotate((A + I(B, C, D) + M[k] + K[j + 48]), 22)
            A, B, C, D = D, A, B, C

        A, B, C, D = (A + AA) & 0xFFFFFFFF, (B + BB) & 0xFFFFFFFF, (C + CC) & 0xFFFFFFFF, (D + DD) & 0xFFFFFFFF
    result = ''.join(f'{x:08x}' for x in (A, B, C, D))
    return result
message = input("Enter the string: ")
hashed = md5(message.encode('utf-8'))
print("MD5 Hash:", hashed)