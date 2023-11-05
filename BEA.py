def gcd(a, b):
    if a == 0:
        return b 
    return gcd(b % a, a)
if __name__ == "__main__":
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  print("gcd(", a, ",", b, ") = ", gcd(a, b))