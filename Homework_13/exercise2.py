def car_price(price, years):
    if years == 0:
        return price
    else:
        price = 0.8 * car_price(price, years-1)
    return round(price, 2)


print(car_price(40000.0, 8))
