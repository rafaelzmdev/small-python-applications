yratio = 0; nratio = 0
while True:
    userinput = input("Please insert an input, '1' or '2', here >>")
    if userinput == "1":
        yratio += 0.69
    elif userinput == "2":
        nratio += 0.69
    else: 
        print("Please insert a correct input.")
    print(yratio - nratio + 25/11*2)