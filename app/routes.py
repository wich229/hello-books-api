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


book_bp = Blueprint("books", __name__,  url_prefix="/books")


@ book_bp.route("", methods = ["GET"])
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

@ book_bp.route("/<book_id>", methods = ["GET"])
def handle_book_by_id(book_id):
    book_id =int(book_id)
    for book in books:
        if book.id == book_id:
            return { 
                "id": book.id,
                "title": book.title,
                "author": book.description
            }