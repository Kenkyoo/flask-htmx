# Flask HTMX Book Recommendations

A simple book recommendation manager built with Flask, SQLAlchemy, and HTMX.

This project demonstrates how to create a dynamic CRUD application using server-rendered HTML and HTMX, without relying on frontend frameworks or custom JavaScript.

## Features

* View all books and authors
* Add new books
* Automatically create authors if they don't exist
* Edit book titles inline
* Delete books
* Dynamic UI updates with HTMX
* SQLite database with SQLAlchemy ORM

## Tech Stack

* Flask
* HTMX
* SQLAlchemy
* Bootstrap
* Gunicorn
* SQLite

## Live Demo

https://flask-htmx-oguy.onrender.com/

## Installation

Clone the repository:

```bash
git clone https://github.com/Kenkyoo/flask-htmx.git
cd flask-htmx
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
flask run
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

The application stores books and authors in a relational database.

When a new book is submitted:

1. The application checks whether the author already exists.
2. If the author exists, the new book is linked to that author.
3. Otherwise, a new author record is created.
4. HTMX updates the table without reloading the page.

Editing and deleting books are also handled through HTMX requests, allowing a smoother user experience while keeping all rendering on the server side.

## Project Structure

```text
flask-htmx/
├── app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── requirements.txt
├── run.py
└── README.md
```

## Learning Goals

This project was created to explore:

* Flask routing and templates
* SQLAlchemy relationships
* HTMX requests and partial updates
* Server-side rendering
* CRUD application patterns

## License

This project is open source and available under the MIT License.
