def number_of_coins(safe_number):
    if safe_number == 1:
        return 1
    else:
        num_of_coins = safe_number-1
    num_of_coins += number_of_coins(safe_number-1)
    return num_of_coins


print(number_of_coins(5))
