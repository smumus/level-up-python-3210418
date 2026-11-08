def get_prime_factors(number):
    factors = []
    for i in range(2, number+1):
        if number % i == 0:
            factors.append(i)
            number = number // i
        else:
            i += 1
    return factors

# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
    print(get_prime_factors(1234))
    print(get_prime_factors(1))
