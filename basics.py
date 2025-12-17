import constants

number_gas = 0
number_oil = 0
gst = 0

print("***Welcome to Gas Station Program!***")
print("Please select the type of purchase:")
option = input("G: Gas \nO: Oil\n>>> ")

option = option.lower()

if option not in ("g", "o"):
  print("Invalid input, you should enter g/G or o/O")
  exit()

if option == "g":
  number_gas = int(input("Enter the number of liters of gas: "))
  if number_gas < 0:
    print("Number of gas liters shoulds be > 0")
    exit()

  province_gas = input("Please enter the 2 letters province abbreviation: ").upper()
  before_discount = int(constants.GAS_LITRE*number_gas)

  if number_gas > 4000:
    price_per_litre = constants.GAS_LITRE - (constants.GAS_LITRE*.10)
  else:
    price_per_litre = constants.GAS_LITRE

  match province_gas:
    case "AB" | "BC" | "MB" | "NT" | "NU" | "QC" | "SK" | "YT":
      gst = constants.GST_ONE/100
    case "ON":
      gst = constants.GST_TWO/100
    case _:
      gst = constants.GST_THREE/100

  after_discount = int(price_per_litre*number_gas)
  gst = gst*after_discount
  total = after_discount + gst

  print(f"{'Product':<10} {'# of Litres':^15} {'Price Before Discount':^22} {'Price After Discount':^22} {'GST':^15} {'Total Price':^15}")
  print(f"{'Gas':<10} {number_gas:^15.1f} {before_discount:^22.1f} {after_discount:^22.1f} {gst:^15.2f} {total:^15.2f}")

if option == "o":
  number_oil = int(input("Enter the number of cases of Oil: "))
  if number_oil < 0:
    print("Number of oil cases should be > 0")
    exit()
  else:
    province_oil = input("Please enter the 2 letters province abbreviation: ").upper()

