def hotel_cost(days):
    return 140 * days
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    car_cost =  40 * days
    if days >= 7:
        return car_cost - 50
    elif days >= 3:
        return car_cost - 20
    else:    
        return car_cost
def trip_cost(city,days,spending_money):
    total = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    return total
    
print trip_cost("Los Angeles",5,600)
