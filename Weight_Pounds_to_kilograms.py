weight_in_lbs = int(input("Enter your weight (lbs): "))
weight_in_kg = weight_in_lbs * 0.45359237
print(weight_in_kg)



while True:
    weight = int(input("Weight: "))
    weight_unit = input('(L)bs or (K)g: ').lower()

    if weight_unit == 'l':
        kilo = round(0.45 * weight)
        print(f"You are {kilo} kilos")
    elif weight_unit == 'k':
        pounds = round(weight / 0.45)
        print(f"You are {pounds} pounds")
