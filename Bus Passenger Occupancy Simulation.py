capacity = 40
passengers = 0
stops = int(input("Number of stops: "))
for stop in range(1, stops + 1):
    boarding = int(input("Passengers boarding at stop " + str(stop) + ": "))
    alighting = int(input("Passengers alighting at stop " + str(stop) + ": "))
    if boarding < 0 or alighting < 0:
        print("Counts cannot be negative")
    elif alighting > passengers:
        print("Invalid: more passengers alighting than on the bus")
    else:
        passengers = passengers - alighting + boarding
        print("Passengers after stop", stop, ":", passengers)
        if passengers > capacity:
            print("CAPACITY VIOLATION")