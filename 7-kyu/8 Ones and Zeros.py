def binary_to_integer(binary_array):
    binary_string = "".join(map(str, binary_array))
    decimal_value = int(binary_string, 2)
    print(decimal_value)


binary_to_integer([0, 1, 0, 1])
