def prime_number(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num):
        if num % i == 0:
            return False
    return True


def even_number(num):
    return num % 2 == 0


def user_input():
    numbers_list = []
    while True:
        user_input = input("Enter the number(EXIT to stop): ")
        if user_input.lower() == 'exit':
            break
        number = int(user_input)
        numbers_list.append(number)
    return numbers_list


if __name__ == "__main__":
    numbers = user_input()
    even_numbers = []
    prime_numbers = []
    for num in numbers:
        if even_number(num):
            even_numbers.append(num)
        if prime_number(num):
            prime_numbers.append(num)
    print("user entered numbers:", numbers)
    print("even numbers: ", even_numbers)
    print("prime numbers: ", prime_numbers)
