#The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

#Assume that the following information are given:
#Price per litre of fuel = 70
#Mileage of the bus in km/litre of fuel = 10
#Price(Rs) per ticket = 80

#The bus runs on multiple routes having different distance in kms and number of passengers.
#Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.
def calculate(distance,no_of_passengers):
    fuel_price_per_litre=70
    milege_per_litre=10
    ticket_price=80
    expenditure=(distance/milege_per_litre)*fuel_price_per_litre
    income=no_of_passengers*ticket_price
    if income>expenditure:
        return income-expenditure
    else:
        return -1
        
#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=1
print(calculate(distance,no_of_passengers))
