country = input('what is your country:')
age = input('enter your age:')
age = int(age)
if country == "Taiwan":
    if age >= 18:
        print('you can drive')
    else:
        print('you cannot drive')
if country == "USA":
    if age >= 16:
        print('you can drive')
    else:
        print('you cannot drive')
else:
    print('you can just choose taiwan or USA')