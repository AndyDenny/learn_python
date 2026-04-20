sandwich_orders = ['Club Sandwich', 'BLT', 'Reuben']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("Finished sandwiches: ", finished_sandwiches)

