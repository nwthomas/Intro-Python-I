def is_prime(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(is_prime(4))  # should return False
print(is_prime(7))  # should return True
