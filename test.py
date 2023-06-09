from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, Author, Genre, Borrower, Review
from sqlalchemy.orm import joinedload


# Create the engine and session
engine = create_engine("sqlite:///books2.db")
Session = sessionmaker(bind=engine)
session = Session()

# START TESTING
##########################################################
# Query the book by ID to get its reviews
# book_id = 2
# book = session.get(Book, book_id)

# # Get the reviews using the get_reviews function
# reviews = book.get_reviews()

# # Print the reviews
# for review in reviews:
#     print(review)


#########################################
# get reviews for a book
def get_borrowers_for_book(book_id):
    book = session.get(Book, book_id)
    if book is None:
        print("Book not found")
        return

    book = (
        session.query(Book)
        .options(joinedload(Book.reviews).joinedload(Review.borrower))
        .filter_by(id=book_id)
        .first()
    )

    if book is None:
        print("Book not found")
        return

    print(f"Reviews for book '{book.title}':")
    for review in book.reviews:
        print(f"Reviewer: {review.borrower.first_name} {review.borrower.last_name}")


book_id = 3  # Replace with the desired book ID
get_borrowers_for_book(book_id)
# #####################################################
# get the list of books in a genre
# def get_genre_by_id(genre_id):
#     genre = session.get(Genre, genre_id)
#     if genre is None:
#         print("Genre not found")
#         return None

#     print(f"Genre ID: {genre.id}, Name: {genre.name}")

#     books = session.query(Book).filter_by(genre_id=genre.id).all()
#     if not books:
#         print("No books found in this genre")
#     else:
#         print("Books in this genre:")
#         for book in books:
#             print(f"Book ID: {book.id}, Title: {book.title}")

#     return genre


# # Example usage
# genre_id = 4  # Replace with the desired genre ID
# genre = get_genre_by_id(genre_id)
# if genre:
#     print(f"Genre Name: {genre.name}")


# #  see output
# Genre ID: 4, Name: area
# Books in this genre:
# Book ID: 3, Title: Deep recognize.
# Book ID: 5, Title: Pressure Mrs rock.
# Book ID: 6, Title: Recognize trade.
# Book ID: 8, Title: Point best magazine bed.
# Book ID: 10, Title: Attention people capital.
# Book ID: 13, Title: Explain real person.
# Book ID: 14, Title: Seven standard.
# Book ID: 20, Title: Another within.
# Book ID: 22, Title: Church course.
# Genre Name: area
# katkimani@DESKTOP-KQE2JKO:~/Development/Code/Mod3/aphase3-books$


# #######################################

# # Get the authors list
# book_id = 10  # Replace with the desired book ID
# get_borrowers_for_book(book_id)

# authors_list = Author.get_authors_list()
# print(authors_list)

#######################################

# Get a book and its author as a tuple
book = session.query(Book).first()
book_tuple = (book.title, book.author.name)

# Print the book tuple
print("Book Tuple:")
print(book_tuple)

#####################################


# Get authors as a dictionary
authors_dict = {}
authors = session.query(Author).all()
for author in authors:
    authors_dict[author.id] = author.name

    # Print the authors dictionary
print("Authors Dictionary:")
print(authors_dict)
