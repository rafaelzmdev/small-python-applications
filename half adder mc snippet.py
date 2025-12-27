while True:
    try:
        n1 = int(input("Please insert the first single digit number here: "))
        n2 = int(input("Please insert the second single digit number here: "))
    except ValueError:
        print("Please insert a valid character. No decimals."); continue
    if n1 & n2 < 10: break
    else: print("The numbers have to be single-digit.")

