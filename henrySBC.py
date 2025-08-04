import tkinter as tk
from tkinter import ttk
from henryDAO import HenryDAO
from HenryInterfaceClasses import Book, Branch

class HenrySBC:
    def __init__(self, window_frame):
        self.window_frame = window_frame 
        self.dao = HenryDAO()
        self.category_label = ttk.Label(self.window_frame, text="Category Selection:")
        self.category_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.category_combobox = ttk.Combobox(self.window_frame, state="readonly")
        self.category_combobox.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_selected)
        self.book_label = ttk.Label(self.window_frame, text="Book Selection:")
        self.book_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.book_combobox = ttk.Combobox(self.window_frame, state="readonly")
        self.book_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="e")
        self.book_combobox.bind("<<ComboboxSelected>>", self.on_book_selected)
        self.price_label = ttk.Label(self.window_frame, text="Price: ")
        self.price_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.price_value_label = ttk.Label(self.window_frame, text="")
        self.price_value_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.tree = ttk.Treeview(self.window_frame, columns=("Branch", "Copies"), show="headings")
        self.tree.heading("Branch", text="Branch Name")
        self.tree.heading("Copies", text="Copies Availlable")
        self.tree.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.load_categories()

    def load_categories(self):
        self.category_list = self.dao.get_categories()
        category_names = [category for category in self.category_list]
        self.category_combobox['values'] = category_names
        if category_names:
            self.category_combobox.current(0)
            self.on_category_selected(None)

    def on_category_selected(self, event):
        chosen_category = self.category_combobox.get()
        self.books = self.dao.get_books_by_category(chosen_category)
        book_titles = [book.title for book in self.books]
        self.book_combobox['values'] = book_titles
        if book_titles:
            self.book_combobox.current(0)
            self.on_book_selected(None)

    def on_book_selected(self, event):
        chosen_book_index = self.book_combobox.current()
        selected_book = self.books[chosen_book_index]
        self.price_value_label.config(text=f"${selected_book.price:.2f}")
        branches = self.dao.get_branch_inventory(selected_book.book_code)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for branch in branches:
            self.tree.insert("", "end", values=(branch.branch_name, branch.num_copies))

