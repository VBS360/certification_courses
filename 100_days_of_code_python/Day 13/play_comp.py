year = int(input("What's your year of birth: "))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a gen Z.")
else:
    print("You are old.")
