def calculate_product(*arg_list):
    prod = 1
    for num in arg_list:
        prod *= num
    return prod
call1 = calculate_product(10, 20, 30)
call2 = calculate_product(*range(1, 6, 2))
print(call1)
print(call2)