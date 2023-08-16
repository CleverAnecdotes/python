def mean(value):
    if type(value) == dict:
        average_temp = sum(value.values()) / len(value)
    else:
        average_temp = sum(value) / len(value)
        #Note that these all need to equal the newly created string, in this case value
    return(average_temp)

Kaufman_Temp = {"Wed" : 95, "Thur" : 107, "Fri" : 108 }


if mean(Kaufman_Temp) > 100:
    print("Too Hot!")
    #You can use elif to add additional potential conditions to an if statement
else: 
    print("Okay fine.")
