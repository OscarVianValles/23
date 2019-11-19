from math import sqrt

def double(x:int) -> int:
    return 2 * x

def largest(x:float, y:float) -> float:
    return x if x > y else y

def verticalline(a:(float, float), b:(float, float)) -> bool:
    return a[0]==b[0] and a[1]!=b[1]

def primes(n:int) -> [int]:
    primes:[int] = []
    curr:int = 1
    check:bool = False

    while(n > 0):
        check = False
        for j in range(2,int(sqrt(curr)) + 1):
            if curr % j == 0:
                check = True
                break
        if check == False:
            primes.append(curr)
            n -= 1
        curr += 1

    return primes

def fibonacci(n:int) -> int:
    fibonacci:[int] = [0, 1]

    while(n > 0):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        n -= 1

    return fibonacci

def sortintegers(l:[int]) -> [int]:
    length:int = len(l)
    holder:int = 0

    for i in range(0, length):
        for j in range(i, length):
            if l[i] > l[j]:
                holder = l[i]
                l[i] = l[j]
                l[j] = holder

    return l

def sublists(l:[int]) -> [[int]]:
    length:int = len(l)
    output:[[int]] = [[]]

    for i in range(0, length + 1):
        for j in range(i + 1, length + 1):
            output.append(l[i:j])

    return output

def fme(b:int,p:int,m:int) -> int:
    exponent = bin(p)[2:]

    if p == 1:
        return 0

    answer:int = 1
    b %= m

    for i in reversed(exponent):
        if(i == "1"):
            answer *= (b % m)

        b = (b % m) ** 2

    return answer % m

def main():
    print(fme(7,1000000000,13));


if __name__ == "__main__":
    main()
