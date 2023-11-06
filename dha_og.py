import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primitive_root(p):
    if p == 2:
        return 1
    if p == 3:
        return 2

    phi_p = p - 1
    for g in range(2, p):
        power = 1
        for i in range(phi_p):
            power = (power * g) % p
        if power == 1:
            return g

def custom_pow(base, exponent, mod):
    result = 1
    for _ in range(exponent):
        result = (result * base) % mod
    return result

def diffie_hellman(p, g, x1, x2):
    y1 = custom_pow(g, x1, p)
    y2 = custom_pow(g, x2, p)

    k1 = custom_pow(y2, x1, p)
    k2 = custom_pow(y1, x2, p)

    return k1, k2

def main():
    while True:
        p = int(input("Enter a prime number (p): "))
        if is_prime(p):
            break
        else:
            print("Please enter a valid prime number.")

    g = find_primitive_root(p)

    x1 = int(input("User 1: Enter a private key (x1): "))
    x2 = int(input("User 2: Enter a private key (x2): "))

    k1, k2 = diffie_hellman(p, g, x1, x2)

    print(f"User 1's private key (x1): {x1}")
    print(f"User 2's private key (x2): {x2}")
    print(f"User 1's shared secret key (k1): {k1}")
    print(f"User 2's shared secret key (k2): {k2}")

if __name__ == "__main__":
    main()
