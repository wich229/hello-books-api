from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        
        
books = [
            Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
            Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
            Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
        ] 


book_dp = Blueprint("books", __name__,  url_prefix="/books")


@ book_dp.route("", methods = ["GET"])
def book_lists():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)