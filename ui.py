from product import Product
from event import Event
import sqlite3
import merchandise_db as db

def display_main_menu_get_choice():
    ''' Display choices and return user's choice'''
    print('''
    1. Edit Merchandise
    2. Edit Events
    3. Enter Sales
    4. Sales Info
    q. Quit Program
    ''')
    choice = input('Enter selection: ')
    return choice

def display_edit_merch_menu():
    '''Display menu, get choice'''
    print('''
        1. Get All Products
        2. Add Product
        3. Edit Price
        4. Edit Quantity
        5. Delete Product
        q. Quit Edit Merchandise Menu
        ''')
    choice = input('Enter selection: ')
    return choice

def display_edit_events_menu():
    '''Display menu, get choice'''
    print('''
        1. Get All Events
        2. Add Event
        3. Edit Event Date
        4. Edit Event Location
        5. Delete Event
        q. Quit Edit Events Menu
        ''')
    choice = input('Enter selection: ')
    return choice

def display_enter_sales_menu():
    '''Display menu, get choice'''
    print('''
        1. Get All Sales
        2. Add Sale
        3. Edit Sale
        4. Delete Sale
        q. Quit Enter Sales Menu
        ''')
    choice = input('Enter selection: ')
    return choice

def display_info_menu():
    '''Display menu, get choice'''
    print('''
            1. Whats the most sold product?
            2. What festival sold the most crystals?
            3. What festival sold the least crystals?
            4. What product sold the least?
            q. Quit Info Menu
            ''')
    choice = input('Enter selection: ')
    return choice


def display_products():
    '''Displays all products'''
    try:
        products = db.get_products()
        for product in products:
            show_product = Product(product[1], product[2], product[3], product[4])
            print('''
            Product Id:  {}{}'''.format(product[0], show_product))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def display_events():
    '''Displays all events'''
    try:
        events = db.get_events()
        for event in events:
            show_event = Event(event[1], event[2], event[3])
            print('''
            Event Id:   {}{}'''.format(event[0], show_event))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def display_sales():
    '''Displays all sales'''
    try:
        sales = db.get_sales()
        for sale in sales:
            print('''
            Sale Id:    {}
            Event Id:   {}
            Product Id: {}
            # Sold:     {}
            '''.format(sale[0], sale[1], sale[2], sale[3]))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return


def add_product():
    '''Adds a product to products table'''
    try:
        product_name = input("Product name: ")
        product_price = float(input("Price: "))
        product_amount = int(input("Amount: "))
        product_desc = input("Description: ")
        product = Product(product_name, product_price, product_amount, product_desc)
        db.insert_product(product)
        message("Added Product")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def edit_price():
    '''Edits a products price'''
    try:
        product_id = int(input("Enter product id: "))
        new_price = float(input("New Price: "))
        db.update_price(product_id, new_price)
        message("Edited Price")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def edit_quantity():
    '''Edits a products quantity'''
    try:
        product_id = int(input("Enter product id: "))
        new_quantity = int(input("New quantity: "))
        db.update_quantity(product_id, new_quantity)
        message("Edited Quantity")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def delete_product():
    '''Deletes a product from products table'''
    try:
        product_id = int(input("Enter product id: "))
        product = db.get_product_by_id(product_id)
        db.remove_product(product_id)
        message("Successfully removed {} from products".format(product[1]))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return


def add_event():
    '''Adds an event to events table'''
    try:
        event_name = input("Event name: ")
        event_date = input("Event date (MM/DD/YYYY): ")
        event_location = input("Event location (city, st): ")
        event = Event(event_name, event_date, event_location)
        db.insert_event(event)
        message("Added Event")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def edit_event_date():
    '''Edits an events date'''
    try:
        event_id = int(input("Enter event id: "))
        new_date = input("New event date (MM/DD/YYYY): ")
        db.update_event_date(event_id, new_date)
        message("Edited Date")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def edit_event_location():
    '''Edits an events location'''
    try:
        event_id = int(input("Enter event id: "))
        new_location = input("New event location (city, st): ")
        db.update_location(event_id, new_location)
        message("Edited Location")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def delete_event():
    '''Deletes an event from events table'''
    try:
        event_id = int(input("Enter event id: "))
        event = db.get_event_by_id(event_id)
        db.remove_event(event_id)
        message("Successfully removed {} from events".format(event[1]))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return


def add_sale():
    '''Adds a sale to the sales tables'''
    try:
        event_id = int(input("Enter event id: "))
        product_id = int(input("Enter product id: "))
        amount_sold = int(input("# Sold: "))
        db.add_sale(event_id, product_id, amount_sold)
        message("Sale Added")
    except sqlite3.IntegrityError as er:
        message("Error: Event ID or Product ID not in database")
        return



def edit_sale():
    '''Edits a sale'''
    try:
        sale_id = int(input("Enter sale id: "))
        amount_sold = int(input("New # Sold: "))
        db.update_sale(sale_id, amount_sold)
        message("Sale Edited")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def delete_sale():
    '''Deletes a sale'''
    try:
        sale_id = int(input("Enter sale id: "))
        sale = db.get_sale_by_id(sale_id)
        db.remove_sale(sale_id)
        message("Sale Deleted")
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return


def most_sold_product():
    '''Displays most sold product'''
    try:
        max_product = 0
        products_sold = db.most_sold_product()
        for product in products_sold:
            if product[1] > max_product:
                max_product = product[1]
                product_id = product[0]
                most_sold = db.get_product_by_id(product_id)
        message('''
        Product: {}
        id:      {}
        sold:    {}
        '''.format(most_sold[1], product_id, max_product))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def festival_sold_most_crystals():
    '''Displays the Festival that sold the most crystals'''
    try:
        max_product = 0
        events = db.festival_sold_most_crystals()
        for event in events:
            if event[1] > max_product:
                max_product = event[1]
                event_id = event[0]
                event_info = db.get_event_by_id(event_id)
        message('''
            Event:    {}
            Date:     {}
            Location: {}
            Sold:     {}
            '''.format(event_info[1], event_info[2], event_info[3], max_product))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def festival_sold_least_crystals():
    '''Displays the Festival that sold the least crystals'''
    try:
        max_product = 1000
        events = db.festival_sold_most_crystals()
        for event in events:
            if event[1] < max_product:
                max_product = event[1]
                event_id = event[0]
                event_info = db.get_event_by_id(event_id)
        message('''
                Event:    {}
                Date:     {}
                Location: {}
                Sold:     {}
                '''.format(event_info[1], event_info[2], event_info[3], max_product))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def least_sold_product():
    '''Returns least sold product'''
    try:
        max_product = 1000
        products_sold = db.most_sold_product()
        for product in products_sold:
            if product[1] < max_product:
                max_product = product[1]
                product_id = product[0]
                least_sold = db.get_product_by_id(product_id)
        message('''
            Product: {}
            Id:      {}
            Sold:    {}
            '''.format(least_sold[1], product_id, max_product))
    except sqlite3.Error as er:
        message("Error: Info not found in database")
        return

def message(msg):
    '''Display a message to the user'''
    print(msg)