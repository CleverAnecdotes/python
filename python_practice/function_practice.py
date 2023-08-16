def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    #creating a new function almost always must end with return. Python is looking for a return at the end.
    return(the_mean)
print (mean([1, 3, 8, 8, 9, 12]))
# define creates a new function, which I'm calling mean and creating a list called my_list
# the_mean is what the function will spit out, then I'm defining what the function will do to create the_mean