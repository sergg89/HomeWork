while True:
    try:
        a = float(raw_input('Enter length of the first cover (a): '))
        b = float(raw_input('Enter width of the first cover (b): '))
        c = float(raw_input('Enter length of the second cover (c): '))
        d = float(raw_input('Enter width of the second cover (d): '))
    except ValueError:
        print('The value must be real number!')
    else:
        if (a < c and b < d) or (a < d and b < c) or (c < a and d < b) or (c < b and d < a):
            print("It's possible")
        else:
            print("It is not possible")
    is_exit = lambda s: True if s.lower() != 'y' and s.lower() != 'yes' else False
    if is_exit(raw_input("Do you want to continue? ")):
        break

