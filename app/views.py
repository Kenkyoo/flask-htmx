from app import app, db
from flask import render_template, request, jsonify
from app.models import Author, Book

@app.route("/", methods=["GET"])
def home():
    books = db.session.query(Book, Author).filter(Book.author_id == Author.author_id).all()
    return render_template("index.html", books=books)

@app.route("/submit", methods=["POST"])
def submit():
    global_book_object = Book()

    title = request.form["title"]
    author_name = request.form["author"]

    author_exists = db.session.query(Author).filter(Author.name == author_name).first()
    print(author_exists)
    # check if author already exists in db
    if author_exists:
        author_id = author_exists.author_id
        book = Book(author_id=author_id, title=title)
        db.session.add(book)
        db.session.commit()
        global_book_object = book
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(author_id=author.author_id, title=title)
        db.session.add(book)
        db.session.commit()
        global_book_object = book

    response = f"""
    <tr>
        <td class="text-white fw-medium">{title}</td>
        <td class="text-muted">{author_name}</td>
        <td class="text-center">
            <button class="btn btn-sm btn-outline-info"
                hx-get="/get-edit-form/{global_book_object.book_id}">
                Edit
            </button>
        </td>
        <td class="text-center">
            <button hx-delete="/delete/{global_book_object.book_id}"
                class="btn btn-sm btn-outline-danger">
                Delete
            </button>
        </td>
    </tr>
    """
    return response

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return ""

@app.route("/get-edit-form/<int:id>", methods=["GET"])
def get_edit_form(id):
    book = Book.query.get(id)
    author = Author.query.get(book.author_id)

    response = f"""
    <tr hx-trigger='cancel' class='editing' hx-get="/get-book-row/{id}">
        <td>
            <input name="title" value="{book.title}" class="form-control form-control-sm text-white" style="background-color: #181825; border: 1px solid #89b4fa;"/>
        </td>
        <td class="text-muted" style="vertical-align: middle;">{author.name}</td>
        <td class="text-center">
            <button class="btn btn-sm btn-outline-secondary" hx-get="/get-book-row/{id}">
                Cancel
            </button>
        </td>
        <td class="text-center">
            <button class="btn btn-sm btn-success" hx-put="/update/{id}" hx-include="closest tr" style="background-color: #a6e3a1; border: none; color: #11111b; font-weight: 600;">
                Save
            </button>
        </td>
    </tr>
    """
    return response

@app.route("/get-book-row/<int:id>", methods=["GET"])
def get_book_row(id):
    book = Book.query.get(id)
    author = Author.query.get(book.author_id)

    response = f"""
    <tr>
        <td class="text-white fw-medium">{book.title}</td>
        <td class="text-muted">{author.name}</td>
        <td class="text-center">
            <button class="btn btn-sm btn-outline-info"
                hx-get="/get-edit-form/{id}">
                Edit
            </button>
        </td>
        <td class="text-center">
            <button hx-delete="/delete/{id}"
                class="btn btn-sm btn-outline-danger">
                Delete
            </button>
        </td>
    </tr>
    """
    return response

@app.route("/update/<int:id>", methods=["PUT"])
def update_book(id):
    db.session.query(Book).filter(Book.book_id == id).update({"title": request.form["title"]})
    db.session.commit()

    title = request.form["title"]
    book = Book.query.get(id)
    author = Author.query.get(book.author_id)

    response = f"""
    <tr>
        <td class="text-white fw-medium">{title}</td>
        <td class="text-muted">{author.name}</td>
        <td class="text-center">
            <button class="btn btn-sm btn-outline-info"
                hx-get="/get-edit-form/{id}">
                Edit
            </button>
        </td>
        <td class="text-center">
            <button hx-delete="/delete/{id}"
                class="btn btn-sm btn-outline-danger">
                Delete
            </button>
        </td>
    </tr>
    """
    return response
