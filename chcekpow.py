#check for any given n value is the power of or not

def is_power_of_k(n, k):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        while n != 1:
            if n % k != 0:
                return False
            n = n // k
    return True
n=int(input('enter the n'))
k=int(input('enter the k'))
print(is_power_of_k(n,k))