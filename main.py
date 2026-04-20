number_seats = int(input("На сколько мест хотите заказать столик? "))
if number_seats > 8:
    print("Придётся подождать... ")
else:
    print("Столик на " + str(number_seats) + " мест готов")