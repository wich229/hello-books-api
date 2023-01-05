from app import db
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, request, jsonify, abort, make_response


books_bp = Blueprint("books", __name__,  url_prefix="/books")
authors_bp = Blueprint("authors", __name__,  url_prefix="/authors")

#################
#  book_routes  #
#################

# create
@ books_bp.route("", methods = ["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)
    
    db.session.add(new_book)
    db.session.commit()
    
    # return make_response(f"Book {new_book.title} successfully created", 201)
    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)


# read books
# @ books_bp.route("", methods = ["GET"])
# def handle_books():
#     books = Book.query.all() # will return a list of instances of books
#     books_response = []
#     for book in books:
#         # Print an Object’s Attributes by dir() or vars()
#         # attributes = vars(book)
#         # print(attributes)
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)


# read books by query param
@ books_bp.route("", methods = ["GET"])
def read_all_books():
    # query by title
    # title_query = request.args.get("title")
    # if title_query:
    #     books = Book.query.filter_by(title = title_query)
    # else:
    #     books = Book.query.all()
    
    # query by sort and sort the data
    # sort_query = request.args.get("sort")
    # if sort_query == "asc":
    #     books = Book.query.order_by(Book.title.asc())
    # if sort_query == "desc":
    #     books = Book.query.order_by(Book.title.desc())
    
        
    #query by title and sort the data
    # sort_query = request.args.get("sort")
    # title_query = request.args.get("title")
    # if title_query and sort_query == "asc":
    #     books = Book.query.filter_by(title = title_query).order_by(Book.title.asc())
    # elif title_query and sort_query == "desc":
    #     books = Book.query.filter_by(title = title_query).order_by(Book.title.desc())
    # elif not title_query and sort_query == "asc":
    #     books = Book.query.order_by(Book.title.asc())
    # elif not title_query and sort_query == "desc":
    #     books = Book.query.order_by(Book.title.desc())
    # elif title_query and not sort_query:
    #     books = Book.query.filter_by(title = title_query)
    # else:
    #     books = Book.query.all()
    
    books_query = Book.query

    title_query = request.args.get("title")
    if title_query:
        books_query = books_query.filter(Book.title.ilike(f"%{title_query}%"))

    sort_query = request.args.get("sort")
    if sort_query == "asc":
        books_query = books_query.order_by(Book.title.asc())
    if sort_query == "desc":
        books_query = books_query.order_by(Book.title.desc())

    books = books_query.all()
        
    #loop into response    
    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response)


# helper function to check book_id
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"msg" : f" {cls.__name__} {model_id} invalid."}, 400))
    
    model = cls.query.get(model_id)
    
    if model:
        return model
        
    abort(make_response({"msg" : f" {cls.__name__} {model_id} not found."}, 404))


# Read_one_book
@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()
    

# Updated_one_book
@books_bp.route("/<book_id>", methods=["PUT"])
def update_one_book(book_id):
    book = validate_model(Book, book_id)
    
    request_body = request.get_json()
    
    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()
    
    return make_response(jsonify(f"Book #{book.id} successfully updated"), 200)


# Delete_one_book
@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book,book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"))


# hard code data version--------------------------

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


# @ books_bp.route("/<book_id>", methods = ["GET"])
# def handle_book_by_id(book_id):
#     book = validate_book(book_id)
#     return { 
#         "id": book.id,
#         "title": book.title,
#         "author": book.description
#     }


###################
#  Author_routes  #
###################

# GET to /authors
@ authors_bp.route("", methods = ["GET"])
def get_authors_by_query():    
    authors_query = Author.query

    name_query = request.args.get("name")
    if name_query:
        authors_query = authors_query.filter(Author.name.ilike(f"%{name_query}%"))

    sort_query = request.args.get("sort")
    if sort_query == "asc":
        authors_query = authors_query.order_by(Author.name.asc())
    if sort_query == "desc":
        authors_query = authors_query.order_by(Author.name.desc())

    authors = authors_query.all()
        
    #loop into response    
    authors_response = []
    for author in authors:
        authors_response.append(author.to_dict())
    return jsonify(authors_response)

# POST to /authors
@ authors_bp.route("", methods = ["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author.from_dict(request_body)
    
    db.session.add(new_author)
    db.session.commit()
    
    # return make_response(f"Book {new_book.title} successfully created", 201)
    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)


