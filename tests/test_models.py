from app.routes import validate_model
from werkzeug.exceptions import HTTPException
from app.models.book import Book
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Book(id = 1,
                    title="Ocean Book",
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Ocean Book"
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_id():
    # Arrange
    test_data = Book(title="Ocean Book",
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] is None
    assert result["title"] == "Ocean Book"
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_title():
    # Arrange
    test_data = Book(id=1,
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] is None
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_description():
    # Arrange
    test_data = Book(id = 1,
                    title="Ocean Book")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Ocean Book"
    assert result["description"] is None

def test_from_dict_returns_book():
    # Arrange
    book_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    new_book = Book.from_dict(book_data)

    # Assert
    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"

def test_from_dict_with_no_title():
    # Arrange
    book_data = {
        "description": "The Best!"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'title'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_no_description():
    # Arrange
    book_data = {
        "title": "New Book"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_extra_keys():
    # Arrange
    book_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }
    
    # Act
    new_book = Book.from_dict(book_data)

    # Assert
    assert new_book.title == "New Book"
    assert new_book.description == "The Best!"
    

def test_validate_model(two_saved_books):
    # Act
    result_book = validate_model(Book, 1)

    # Assert
    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"

def test_validate_model_missing_record(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "3")
    
def test_validate_model_invalid_id(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "cat")