# Henry Bookstore Database Application

A Python GUI application that connects to a MySQL relational database to search and explore a catalog of books by author, category, or publisher. This project demonstrates full-stack database integration with Python, applying principles of modular design, GUI development with `tkinter`, and database abstraction using the DAO pattern.

## Project Summary

This application is a front-end interface for a fictional bookstore database. Users can navigate through a tabbed interface to:

- Search for books by **Author**
- Browse available books by **Category**
- View published titles by **Publisher**

Each tab dynamically updates content based on user selections. All database access is handled through a dedicated DAO layer, ensuring clear separation of concerns and maintainability.

The project simulates real-world database interaction and GUI design and is suitable as a demonstration of full-stack database-driven application development in Python.

## Key Features

- Modular GUI architecture using `tkinter.Notebook` (tabbed interface)
- Real-time dynamic updates based on user input (e.g., book lists and inventory per author)
- Clean separation between GUI and data logic using the DAO pattern
- Uses custom data interface classes to encapsulate author, book, and inventory data
- Robust SQL schema with populated tables including authors, books, publishers, and inventory levels
- Designed with usability in mind: ComboBoxes, TreeViews, and Labels dynamically populated and updated

## Technologies Used

- Python 3
- tkinter (GUI)
- MySQL (RDBMS)
- mysql-connector-python (Python–MySQL integration)

## Project Structure

henry-bookstore/
├── Henry.py # Main application launcher (GUI)
├── henrySBA.py # GUI: Search by Author tab
├── henrySBC.py # GUI: Search by Category tab
├── henrySBP.py # GUI: Search by Publisher tab
├── henryDAO.py # Data Access Object (database layer)
├── HenryInterfaceClasses.py # Data model classes (Author, Book, etc.)
├── Henry.sql # SQL schema and data (books, authors, etc.)
└── henryPython.pdf # Assignment specification and requirements


## Setup Instructions

1. **Install MySQL** and load the provided schema:
   - Use the script `Henry.sql` in MySQL Workbench or via CLI to create and populate the database.

2. **Install required Python package:**
   ```bash
   pip install mysql-connector-python
3. **Configure the DAO connection:
   - Update the connection settings in henryDAO.py:
  
     mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_password",
    database="henry_books"
)

4. **Run the application:
   - python Henry.py
  
Example Use Case
When the user opens the app, the Search by Author tab displays a list of authors. Selecting an author updates a list of their books. Clicking on a book shows which branches have it in stock and at what quantity, along with the book’s price. The other tabs behave similarly for categories and publishers.

Skills Demonstrated:
GUI development in Python
SQL schema design and relational modeling
OOP and modular programming
Event-driven programming (tkinter callbacks)
Data abstraction and software architecture using DAO
Integration of frontend and backend components
