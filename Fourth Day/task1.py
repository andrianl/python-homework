while True:
    number=int(input("Введіть,  будь ласка, число:"))
    if number<=1000:
        binary=bin(number)
        octagon=oct(number)
        hexagon=hex(number)
        print('{:>10}'.format('bin'), '{:>20}'.format('oct'), '{:>30}'.format('dec'), '{:>40}'.format('hex'))
        print('{:>10}'.format(str(binary)),'{:>20}'.format(str(octagon)), '{:>30}'.format(str(number)), '{:>40}'.format(str(hexagon)))
        break
        pass
    else:
        print("Введіть число менше 1000!")
        continue
        pass
