def validate_number(number):
    if type(number) != int:
        return "number is not integer."
    elif number < 0:
        return "The number must be greater than 0."
    else:
        people = number
        van = 0
        car = 0

        while people > 0:
            if people >= 11:
                people -= 11
                van += 1
            elif people >= 4:
                people -= 4
                car += 1
            else:
                break
        return (people, van, car)


def display_result(result):
    people, van, car = result
    print("Number of used vans: ", van ,"vans")
    print("Number of used cars: ", car ,"cars")
    print("Number of people left: ", people ,"people")

    
    
