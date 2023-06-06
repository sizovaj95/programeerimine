import re


def minprice(price_list, place_list):
    min_price = min(price_list)
    for i, price in enumerate(price_list):
        if price == min_price:
            min_place = place_list[i]
            print(f"Minimum price {min_price} EUR is in {min_place}.")
            break


def avgprice(price_list):
    return sum(price_list) / len(price_list)


def pricerange(price_list):
    return avgprice(price_list) - min(price_list)


def main():
    try:
        with open("food.txt", "r") as f:
            menu = f.read()
            menu = menu.split('\n')
        user_input = input("What dish would you like to have? ")
        price_list = []
        place_list = []
        for line in menu:
            if user_input.lower() in line.lower():
                parts = re.split(r' - |, ', line)
                place = parts[0]
                price = float(parts[2])
                place_list.append(place)
                price_list.append(price)
                print(f"You can have {user_input} in {place} for {price} EUR.")

        if not place_list:
            print("This dish is not served in restaurants of Narva.")
        else:
            print('\n')
            price_range = pricerange(price_list)
            print(f"Difference between minimum and average prices is {price_range} EUR.")
            minprice(price_list, place_list)
            print(f"Average price is {avgprice(price_list)} EUR.")

    except FileNotFoundError:
        print("File food.txt not found!")


main()