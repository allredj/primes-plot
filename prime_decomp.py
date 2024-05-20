## give the prime decomposition of a number
def prime_decomp(n):
    """
    Given a number, find the prime decomposition of the number.
    :param n: The number to find the prime decomposition of.
    :return: The prime decomposition of n.
    """
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors


# main function
def main():
    # Test the prime_decomp function
    for i in range(1, 2001):
        print(f"prime_decomp({i}) = {prime_decomp(i)}")


if __name__ == "__main__":
    main()
