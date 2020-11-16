def wedding_chow(chow):
    """
    At the reception of GeekTutor's wedding, guests are to be served. A complete chow has rice(r), stew(s), meat(m), fish(f) and a drink(d).
    The function 'wedding_chow' takes in a string input(representing the supplies available) and returns a tuple containing the number of guests that can receive complete chow as an integer and the leftover chow as a string arranged in order(rsmfd).
    """
    if isinstance(chow,str):
        chow1 = list(chow)
        rice,stew,meat,fish,drink = ([] for i in range(5))  #Creates empty lists for the chows.
        poison_left_over_rice,poison_left_over_stew,poison_left_over_meat,poison_left_over_fish,poison_left_over_drink = ([] for i in range(5))  #Creates empty lists for the leftover with strange chow.
        #Adds every chow to its corresponding list and if there is a strange chow it returns a tuple containing 0(zero) as the number of guests that can receive complete chow and the leftover without the strange chow.
        for i in chow:
            if i=='r':
                rice.append(i)
            elif i=='s':
                stew.append(i)
            elif i=='m':
                meat.append(i)
            elif i=='f':
                fish.append(i)
            elif i=='d':
                drink.append(i)
            else:
                chow1.remove(i)
                for i in chow1:
                    if i=='r':
                        poison_left_over_rice.append(i)
                    elif i=='s':
                        poison_left_over_stew.append(i)
                    elif i=='m':
                        poison_left_over_meat.append(i)
                    elif i=='f':
                        poison_left_over_fish.append(i)
                    elif i=='d':
                        poison_left_over_drink.append(i)
                    total_poison_left_over = poison_left_over_rice+poison_left_over_stew+poison_left_over_meat+poison_left_over_fish+poison_left_over_drink
                return (0,"".join(total_poison_left_over))
                
        complete_chow = min(len(rice),len(stew),len(meat),len(fish),len(drink)) #Finds the length of the chow with the least supplies.

        #Collates the supplies that would make a complete chow.
        new_rice = rice[0:complete_chow]
        new_stew = stew[0:complete_chow]
        new_meat = meat[0:complete_chow]
        new_fish = fish[0:complete_chow]
        new_drink = drink[0:complete_chow]
        new_chow = rice+stew+meat+fish+drink
        left_over_rice,left_over_stew,left_over_meat,left_over_fish,left_over_drink = ([]  for i in range(5))   #Creates empty lists for the left over chows.

        #Adds all left over chows to its corresponding list in the order(rsmfd).
        for i in rice:
            if not i in new_rice or new_rice.remove(i):
                left_over_rice.append(i)
        for j in stew:
            if not j in new_stew or new_stew.remove(j):
                left_over_stew.append(j)
        for k in meat:
            if not k in new_meat or new_meat.remove(k):
                left_over_meat.append(k)
        for l in fish:
            if not l in new_fish or new_fish.remove(l):
                left_over_fish.append(l)
        for m in drink:
            if not m in new_drink or new_drink.remove(m):
                left_over_drink.append(m)
        total_left_overs  = left_over_rice+left_over_stew+left_over_meat+left_over_fish+left_over_drink
        total_left_overs = "".join(total_left_overs)    #Joins the left over chows to become string form.
    else:
        return "Invalid input. Only string of supplies are allowed."
    
    return (complete_chow,total_left_overs)

print(wedding_chow('rsmfdrsmfdrsm'))
print(wedding_chow('fdrsmssrrdr'))
