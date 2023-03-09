def fibonacci(fibonacci_length):
    fibonacci_list = []
    i = 0
    while i < int(fibonacci_length):
        if i == 0 or i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
        i += 1
    return fibonacci_list


print(fibonacci(input("Enter the length of the fibonacci series: ")))
