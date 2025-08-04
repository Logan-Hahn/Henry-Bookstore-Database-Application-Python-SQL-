import mysql.connector
from HenryInterfaceClasses import Author, Book, Branch

class HenryDAO:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            database='comp3421', 
            user='root',
            password='Santaclaus1')
        self.cursor = self.conn.cursor()

    def get_author_data(self):
        author_query = "SELECT author_num, author_first, author_last FROM henry_author"
        self.cursor.execute(author_query)
        author_results = self.cursor.fetchall()
        author_list = []
        for (author_num, author_first, author_last) in author_results:
            if self.check_for_books(author_num):
                author_list.append(Author(author_num, author_first, author_last))
        return author_list

    def check_for_books(self, author_num):
        check_books_query = "SELECT COUNT(*) FROM henry_wrote WHERE author_num = %s"
        self.cursor.execute(check_books_query, (author_num,))
        book_count = self.cursor.fetchone()[0]
        return book_count > 0

    def get_books_by_author(self, author_num):
        book_query = "SELECT b.book_code, b.title, b.price FROM henry_book b JOIN henry_wrote w ON b.book_code = w.book_code WHERE w.author_num = %s"
        self.cursor.execute(book_query, (author_num,))
        book_results = self.cursor.fetchall()
        
        book_list = []
        for (book_code, title, price) in book_results:
            book_list.append(Book(book_code, title, price))
        return book_list

    def get_branch_inventory(self, book_code):
        inventory_query = "SELECT br.branch_name, inv.on_hand FROM henry_branch br JOIN henry_inventory inv ON br.branch_num = inv.branch_num WHERE inv.book_code = %s"
        self.cursor.execute(inventory_query, (book_code,))
        inventory_results = self.cursor.fetchall()
        branch_list = []
        for (branch_name, on_hand) in inventory_results:
            branch_list.append(Branch(branch_name, on_hand))
        return branch_list
    
    def get_categories(self):
        category_query = "SELECT DISTINCT type FROM henry_book"
        self.cursor.execute(category_query)
        category_results = self.cursor.fetchall()
        category_list = [category[0] for category in category_results]
        return category_list

    def get_books_by_category(self, category):
        book_category_query = "SELECT book_code, title, price FROM henry_book WHERE type = %s"
        self.cursor.execute(book_category_query, (category,))
        category_book_results = self.cursor.fetchall()
        category_book_list = []
        for (book_code, title, price) in category_book_results:
            category_book_list.append(Book(book_code, title, price))
        return category_book_list

    def get_publishers(self):
        publisher_query = "SELECT DISTINCT publisher_name FROM henry_publisher"
        self.cursor.execute(publisher_query)
        publisher_results = self.cursor.fetchall()
        publisher_list = [publisher[0] for publisher in publisher_results]
        return publisher_list

    def get_books_by_publisher(self, publisher_name):
        book_publisher_query = "SELECT b.book_code, b.title, b.price FROM henry_book b JOIN henry_publisher p ON b.publisher_code = p.publisher_code WHERE p.publisher_name = %s"
        self.cursor.execute(book_publisher_query, (publisher_name,))
        publisher_book_results = self.cursor.fetchall()
        publisher_book_list = []
        for (book_code, title, price) in publisher_book_results:
            publisher_book_list.append(Book(book_code, title, price))
        return publisher_book_list

    def close(self):
        self.cursor.close()
        self.conn.close()
