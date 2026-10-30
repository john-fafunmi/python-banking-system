def add_library(library, book_name, author, genre, genres):
    add_book = book_name.lower()
    add_author = author.title()
    clean_genre = genre.strip().title()
    if add_book not in library:
        library[add_book] = {
                "author": add_author, "availability": True
        }
        genres.add(clean_genre)
        print(f"Successfully added {add_book.title()} to the library!")
    else:
        print(f"'{add_book.title()}' is already in the library.")
    
    


def remove_book(library, book):
    remove_book_name = book.lower()
    if remove_book_name in library:
        library.pop(remove_book_name, None)
        print(f"'{remove_book_name.title()}' has been removed successfully from the library!")
    else:
        print(f"'{remove_book_name.title()}' is not in the library.")
    
    
def view_library(library):
    avail = ""
    print(f"Your Library has {len(library)} books:")
    for book, info in library.items():
        print(f"Book name: {book.title()}")

        if info["availability"] == True:
            avail = "On Shelf"
        else:
            avail = "Checked Out"
        print(f"Author: {info['author']}")
        print(f"Availability: {avail}")
    print(" ")

def view_genres(genres):
    print(f"Your library has {len(genres)} available genres: ")
    for item in genres:
        print(f"Genre: {item.title()}")


def main():
    library = {
    "the lightning thief": {"author": "Rick Riordan", "availability": True},
    "blade": {"author": "Wendy Walker", "availability": True}
}

    genres = {"thriller", "fantasy", "historical fiction"}

    user = input("What is your name? ").title()
    print(f"Hello {user}! Welcome to your Library.")
    while True:
        print("Options:\nPress 1 to add to library\nPress 2 to remove from library\nPress 3 to view your library\nPress 4 to view the genres\nPress 5 to exit")
        interaction = (input("Enter number here: ")).strip()
        if interaction == "1":
            ask1 = input("What is the name of the book? ")
            ask2 = input("Who is the author of the book? ")
            ask3 = input("What is the genre of the book? ")
            add_library(library, ask1, ask2, ask3, genres)
        elif interaction == "2":
            ask1 = input("What is the name of book to remove? ")
            remove_book(library, ask1)
        elif interaction == "3":
            view_library(library)
        elif interaction == "4":
            view_genres(genres)
        elif interaction == "5":
            print("You have exitted")
            break
        else:
            print("Please type a number from (1-5): ")
    

main()



