# Task 1: Formatting Flight Itineraries

#                Person     Origin     Destination   Name    Origin   Destination
tuples_list = [("Bill", "Los Angeles", "Phoenix"), ("Jimmy", "Boston", "Miami")] # A list containing tuples with passenger information.

def itinerary(): # Defining a function that creates an itinerary.
    i = 1 # Creating our starting value saved under the variable i.
    for passenger in tuples_list: # Iterates over the information saved in the list tuples_list.
        print(f"Itinerary {i}", passenger[0], '- from', passenger[1], "to", passenger[2]) # Prints our string with the itinerary number as well as the passenger name, start point, and destination by the index selected.
        i += 1 # Adds 1 to the variable i each time so that it continues in a numeric sequence counting up.
itinerary() # Calling our funciton.
