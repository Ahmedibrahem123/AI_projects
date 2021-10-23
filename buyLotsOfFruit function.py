
def fruits():
    list = input(" Enter your list of Fruits: ").replace(" ", "").split(',')
    list_of_fruits = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0), ('orange', 5.0), ('banana', 6.5)]
    cost = 0
    out_str = '['
    for item in list:
        flag = False
        for (x, y) in list_of_fruits:
            if item == x:
                cost += y
                out_str = out_str + '(' + x + ',' + str(y) + '),'
                flag = True
        if not flag:
            print(" Error massage  ")
            return None
    print("Cost of" + out_str[:-1] + "] is " + str(cost))

fruits()