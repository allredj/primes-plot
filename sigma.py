# Given a number, find the sum of all its factors.

def sigma(n):
    """
    Given a number, find the sum of all its factors including the number itself.
    :param n: The number to find the factors of.
    :return: The sum of all factors of n.
    """
    factors = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sum(factors)

# main function
def main():
    # Test the sum_factors function
    for i in range(1, 201):
        print(f"sigma({i}) = {sigma(i)}")
        print(f"half_sigma({i}) = {sigma(2*i) - 2*i - sigma(i)}")
        print(f"abundance({i}) = {sigma(i) - 2*i}")
        print(f"slope({i}) = {sigma(2*i) - 2*i - sigma(i)}/{i}")
        print(f"-------------------")

if __name__ == "__main__":
    main()