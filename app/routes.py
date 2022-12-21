from app import db
from app.models.book import Book
from flask import Blueprint, request, jsonify, abort, make_response


books_bp = Blueprint("books_bp", __name__,  url_prefix="/books")

# create
@ books_bp.route("", methods = ["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(
                    # id = request_body["id"],
                    title = request_body["title"],
                    description = request_body["description"]
                    )
    
    db.session.add(new_book)
    db.session.commit()
    
    return make_response(f"Book {new_book.title} successfully created", 201)


@ books_bp.route("", methods = ["GET"])
def handle_books():
    books = Book.query.all() # will return a list of instances of books
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
    

# @ books_bp.route("", methods = ["GET"])
# def book_lists():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)


# def validate_book(book_id):
#     try:
#         book_id =int(book_id)
#     except:
#         abort(make_response({"msg" : f" book {book_id} invalid."}, 400))
    
#     for book in books:
#         if book.id == book_id:
#             return book
            
#     abort(make_response({"msg" : f" book {book_id} not found"}, 404))
    


# @ books_bp.route("/<book_id>", methods = ["GET"])
# def handle_book_by_id(book_id):
#     book = validate_book(book_id)
#     return { 
#         "id": book.id,
#         "title": book.title,
#         "author": book.description
#     }
