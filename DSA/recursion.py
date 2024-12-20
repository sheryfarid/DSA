# def find_num(n):
#     if n == 1:
#         return n 
#     return n * find_num(n-1)

# if __name__ == "__main__":
#     print(find_num(5))


# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0

# # Example usage
# if __name__ == "__main__":
#     print(is_power_of_two(128))  # True


def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Example usage
if __name__ == "__main__":
    test_cases = [0, 1, 3, 9,18, 27, 81, 10, 100]
    for num in test_cases:
        print(f"{num}: {is_power_of_three(num)}")