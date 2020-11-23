def fooTemp(val):
    if (val > 25):
        return "Hot"
    elif (val>=15) and (val<=25):
        return "Warm"
    else:
        return "Cold"


def foo(val):
    if (val>7):
        return "Warm"
    else:
        return "Cold"

def foo(val):
    return (len(val) > 8)

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean



#students_grades = {"Mary":9.1 , "Sim":8.8, "John":7.5}
#print(mean(students_grades))
#monday_temp = [8.8, 9.1, 9.9]
#print(mean(monday_temp))

print(foo("myverylongpass"))
