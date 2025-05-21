import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3

class GUI(Gtk.Window):
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_default_size(600, 400)
        self.window.set_title("Interfejs Biblioteki")

        self.create_table()
        self.refresh_table()
        
        self.create_buttons()

        self.create_dialog()

        self.add_to_window()

        self.window.show_all()

    def create_table(self):
        self.table = Gtk.Table(5, 2)
        self.table.set_col_spacings(5)
        self.table.set_row_spacings(5)

        self.table.attach(Gtk.Label("Tytuł"), 0, 1, 0, 1)
        self.table.attach(Gtk.Label("Autor"), 1, 2, 0, 1)
        self.table.attach(Gtk.Label("Rok"), 2, 3, 0, 1)

    def refresh_table(self):
        con = sqlite3.connect("baza.db")
        cur = con.cursor()
        cur.execute("SELECT title, author, year FROM books")
        rows = cur.fetchall()
        con.close()

        # Usuwanie wcześniejszych danych z tabeli
        for child in self.table.get_children():
            self.table.remove(child)

        # Dodawanie nowych danych do tabeli
        for row, data in enumerate(rows):
            for col, value in enumerate(data):
                self.table.attach(Gtk.Label(value), col, col+1, row+1, row+2)

    def create_buttons(self):
        self.edit_button = Gtk.Button("Edytuj")
        self.edit_button.connect("clicked", self.on_edit_clicked)

        self.delete_button = Gtk.Button("Usuń")
        self.delete_button.connect("clicked", self.on_delete_clicked)

        self.add_button = Gtk.Button("Dodaj")
        self.add_button.connect("clicked", self.on_add_clicked)

def create_dialog(self):
    self.dialog = Gtk.Dialog("Szczegóły książki", None, Gtk.DIALOG_MODAL | Gtk.DIALOG_DESTROY_WITH_PARENT, (Gtk.STOCK_OK, Gtk.RESPONSE_ACCEPT))
    self.dialog.set_default_size(250, 150)

    self.title_label = Gtk.Label("Tytuł: ")
    self.title_entry = Gtk.Entry()
    self.title_entry.set_editable(False)
    self.author_label = Gtk.Label("Autor: ")
    self.author_entry = Gtk.Entry()
    self.author_entry.set_editable(False)
    self.year_label = Gtk.Label("Rok: ")
    self.year_entry = Gtk.Entry()
    self.year_entry.set_editable(False)

    self.dialog.vbox.add(self.title_label)
    self.dialog.vbox.add(self.title_entry)
    self.dialog.vbox.add(self.author_label)
    self.dialog.vbox.add(self.author_entry)
    self.dialog.vbox.add(self.year_label)
    self.dialog.vbox.add(self.year_entry)

def add_to_window(self):
    self.main_container = Gtk.VBox()
    self.button_container = Gtk.HBox()

    self.main_container.pack_start(self.table)

    self.button_container.pack_start(self.edit_button)
    self.button_container.pack_start(self.delete_button)
    self.button_container.pack_start(self.add_button)

    self.main_container.pack_start(self.button_container)
    self.window.add(self.main_container)

def on_edit_clicked(self, button):
    selected_row = self.table.get_focus()[0]
    if selected_row is not None:

        con = sqlite3.connect("baza.db")
        cur = con.cursor()
        cur.execute("SELECT title, author, year FROM books WHERE rowid = ?", (selected_row,))
        row = cur.fetchone()
        con.close()


        self.title_entry.set_text(row[0])
        self.author_entry.set_text(row[1])
        self.year_entry.set_text(row[2])


        self.dialog.run()
        self.dialog.hide()
    else:
        error_dialog = Gtk.MessageDialog(self.window, Gtk.DIALOG_MODAL, Gtk.MESSAGE_ERROR, Gtk.BUTTONS_OK, "Nie wybrano żadnego rekordu!")
        error_dialog.run()
        error_dialog.destroy()

def on_delete_clicked(self, button):
    selected_row = self.table.get_focus()[0]
    if selected_row is not None:
        con = sqlite3.connect("baza.db")
        cur = con.cursor()
        cur.execute("DELETE FROM books WHERE rowid = ?", (selected_row,))
        con.commit()
        con.close()

        self.refresh_table()
    else:
        error_dialog = Gtk.MessageDialog(self.window, Gtk.DIALOG_MODAL, Gtk.MESSAGE_ERROR, Gtk.BUTTONS_OK, "Nie wybrano żadnego rekordu!")
        error_dialog.run()
        error_dialog.destroy()

def on_add_clicked(self, button):
    add_dialog = Gtk.Dialog("Dodawanie książki", None, Gtk.DIALOG_MODAL | Gtk.DIALOG_DESTROY_WITH_PARENT, (Gtk.STOCK_OK, Gtk.RESPONSE_ACCEPT, Gtk.STOCK_CANCEL, Gtk.RESPONSE_REJECT))
    add_dialog.set_default_size(250, 150)

    title_label = Gtk.Label("Tytuł: ")
    title_entry = Gtk.Entry()
    author_label = Gtk.Label("Autor: ")
    author_entry = Gtk.Entry()
    year_label = Gtk.Label("Rok: ")
    year_entry = Gtk.Entry()

    add_dialog.vbox.add(title_label)
    add_dialog.vbox.add(title_entry)
    add_dialog.vbox.add(author_label)
    add_dialog.vbox.add(author_entry)
    add_dialog.vbox.add(year_label)
    add_dialog.vbox.add(year_entry)

    response = add_dialog.run()
    if response == Gtk.RESPONSE_ACCEPT:
        title = title_entry.get_text()
        author = author_entry.get_text()
        year = year_entry.get_text()

        con = sqlite3.connect("baza.db")
        cur = con.cursor()
        cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        con.commit()
        con.close()

        self.refresh_table()

    add_dialog.destroy()

def refresh_table(self):
    con = sqlite3.connect("baza.db")
    cur = con.cursor()
    cur.execute("SELECT title, author, year FROM books")
    rows = cur.fetchall()
    con.close()

    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            self.table.set_text(i, j, item)

r = GUI()
Gtk.main()
    



