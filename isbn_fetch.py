import re
import requests

def is_valid_isbn(isbn):
    """Validate ISBN (10 or 13 digits)."""
    isbn = isbn.replace("-", "").strip()
    return re.match(r'^\d{10}(\d{3})?$', isbn) is not None

while True:
    try:
        print("\nOptions:")
        print("1. Fetch book details by ISBN")
        print("2. Fetch book details by name")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            isbn = input("Enter ISBN: ").strip()
            if not is_valid_isbn(isbn):
                print("Invalid ISBN. Please enter a 10 or 13-digit ISBN.")
                continue

            url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            book_key = f"ISBN:{isbn}"

            if book_key in data:
                book = data[book_key]
                title = book.get("title", "N/A")
                authors = ", ".join(author["name"] for author in book.get("authors", [])) or "Unknown"

                print(f"\nTitle: {title}\nAuthors: {authors}\n")
            else:
                print("No details found for the given ISBN.")

        elif choice == "2":
            name = input("Enter book name: ").strip()
            if not name:
                print("Book name cannot be empty.")
                continue

            url = f"https://openlibrary.org/search.json?title={name}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get("docs"):
                book = data["docs"][0]  # Take the first matching result
                title = book.get("title", "N/A")
                authors = ", ".join(book.get("author_name", [])) or "Unknown"
                isbn = book.get("isbn", ["N/A"])[0]

                print(f"\nTitle: {title}\nAuthors: {authors}\nISBN: {isbn}\n")
            else:
                print("No details found for the given book name.")

        elif choice == "3":
            print("Exiting the program...")
            exit()

        else:
            print("Invalid choice. Please select a valid option.")

    except (requests.RequestException, KeyError, TypeError):
        print("An error occurred while fetching book details. Please try again.")

    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()

