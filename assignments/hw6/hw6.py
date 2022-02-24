def cash_converter():
    dollars = eval(input("enter an integer:"))
    print("That is ${}.{:0>2}".format(dollars, "00"))
