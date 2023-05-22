



if __name__ == "__main__":
    print()
    print()
    print("          *** Stock Analysis ***")
    print()
    print("Please Enter Your Stock Details (As per year) ")
    print()

    peratio = int(input("Price to Earnings Ratio (PE) : "))
    divident = int(input("Divident Yeild (%) : "))
    roe = int(input("Return on Equity (ROE) (%): "))
    debt = int(input("Debt to Equity Ratio "))



    print()


    if (peratio>15 and peratio<25):
        print("PE Ratio is Best")
    elif (peratio>10 and peratio<15):
        print("PE Ratio is Good")
    elif (peratio>25):
        print("PE Ratio is Worse")
    elif (peratio>25):
        print("PE Ratio is Worse")
    else:
        print("PE Ratio is Worse")




    if (divident>3):
        print("Divident is Best")
    else:
        print("Divident is Worse")
        


    if (roe>15 and roe<25):
        print("ROE is Best")
    else:
        print("ROE is Worse")


    if (debt<1.5):
        print("Debt is Good")
    else:
        print("Debt is Worse")


    
