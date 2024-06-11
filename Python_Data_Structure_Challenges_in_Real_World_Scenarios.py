# Task 1: Library System Enhancement
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] # Our list of tuples containing book titles and authors.

def main(): # main function
    while True: # while loop to execute code until condition is False.
        user = input('''Please select an option
                 1. Add new book
                 2. View list
                 3. Quit
                 ''') # User input select menu.
        if user == '1':
            new_book() # calling new_book() function
        elif user == '2':
            print(library) # Simply printing the list library for the user to see.
        elif user == '3':
            print("Thank you, have a good day.")
            break # Breaks out of the while loop.
        else:
            continue # Goes back to the beginning of the function, bringing the user back to the main menu if they enter an invalid input.

def new_book(): # Creating a function to add a new book.
    book_input = input("What is the title of the book? ").title() # The .title() method takes the user input and returns it with the first letter of each word capitalized.
    for title in library: 
        if book_input in title: # Iterates over the titles in library to see if the book title the user enters is already in the list or not.
            print("Book already found in library.")
            return book_input # Takes the user back to the beginning of the function if the book title is already in the list.  
    author_input = input("Who is the author of this book? ").title()
    new_book_tuple =(book_input, author_input) # Creating a new tuple consisting of the user inputs for new title and author.
    library.append(new_book_tuple) # Appending the tuple to the list library.

main() # Calling our main function.