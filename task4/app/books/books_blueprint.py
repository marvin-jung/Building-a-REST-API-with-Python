from flask import Blueprint, jsonify, request

books_blueprint = Blueprint('books_blueprint', __name__, url_prefix="/books")

books = [
    {
        "id": 1,
        "title": "Dune",
        "author": "Frank Herbert"
    },
    {
        "id": 2,
        "title": "How to Win Friends & Influence People",
        "author": "Dale Carnegie"
    },
    {
        "id": 3,
        "title": "The Giver",
        "author": "Lois Lowry"
    },
]


@books_blueprint.route("")
def get_books():
    serialised = {
        "books": books
    }

    return jsonify(serialised)


@books_blueprint.route("<int:uid>")
def get_book(uid):
    book = next(book for book in books if book["id"] == uid)
    return jsonify(book)


@books_blueprint.route("", methods=["POST"])
def post_book():
    request_json = request.get_json()
    try:
        title = request_json['title']
        author = request_json['author']
    except KeyError:
        return "Please provide a title and author.", 400

    new_book = {
        "id": books[-1]["id"] + 1,
        "title": title,
        "author": author
    }
    books.append(new_book)

    serialised = {
        "books": books
    }

    return jsonify(serialised)

