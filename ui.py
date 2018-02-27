from product import Product
from event import Event
import merchandise_db as db

def display_main_menu_get_choice():
    ''' Display choices and return user's choice'''
    print('''
    1. Edit Merchandise
    2. Edit Events
    3. Enter Sales
    4. Helpful Info
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

def display_products():
    '''Displays all products'''
    products = db.get_products()
    for product in products:
        show_product = Product(product[1], product[2], product[3], product[4])
        print('''
        Product Id:  {}{}'''.format(product[0], show_product))

def display_events():
    '''Displays all events'''
    events = db.get_events()
    for event in events:
        show_event = Event(event[1], event[2], event[3])
        print('''
        Event Id:   {}{}'''.format(event[0], show_event))

def display_sales():
    '''Displays all sales'''
    sales = db.get_sales()
    for sale in sales:
        print('''
        Sale Id:    {}
        Event Id:   {}
        Product Id: {}
        # Sold:     {}
        '''.format(sale[0], sale[1], sale[2], sale[3]))

def add_product():
    '''Adds a product to products table'''
    product_name = input("Product name: ")
    product_price = float(input("Price: "))
    product_amount = int(input("Amount: "))
    product_desc = input("Description: ")
    product = Product(product_name, product_price, product_amount, product_desc)
    db.insert_product(product)
    message("Added Product")

def edit_price():
    '''Edits a products price'''
    product_id = int(input("Enter product id: "))
    new_price = float(input("New Price: "))
    db.update_price(product_id, new_price)
    message("Edited Price")

def edit_quantity():
    '''Edits a products quantity'''
    product_id = int(input("Enter product id: "))
    new_quantity = int(input("New quantity: "))
    db.update_quantity(product_id, new_quantity)
    message("Edited Quantity")

def delete_product():
    '''Deletes a product from products table'''
    product_id = int(input("Enter product id: "))
    product = db.get_product_by_id(product_id)
    db.remove_product(product_id)
    message("Successfully removed {} from products".format(product[1]))

def add_event():
    '''Adds an event to events table'''
    event_name = input("Event name: ")
    event_date = input("Event date (MM/DD/YYYY): ")
    event_location = input("Event location (city, st): ")
    event = Event(event_name, event_date, event_location)
    db.insert_event(event)
    message("Added Event")

def edit_event_date():
    '''Edits an events date'''
    event_id = int(input("Enter event id: "))
    new_date = input("New event date (MM/DD/YYYY): ")
    db.update_event_date(event_id, new_date)
    message("Edited Date")

def edit_event_location():
    '''Edits an events location'''
    event_id = int(input("Enter event id: "))
    new_location = input("New event location (city, st): ")
    db.update_location(event_id, new_location)
    message("Edited Location")

def delete_event():
    '''Deletes an event from events table'''
    event_id = int(input("Enter event id: "))
    event = db.get_event_by_id(event_id)
    db.remove_event(event_id)
    message("Successfully removed {} from events".format(event[1]))

def add_sale():
    '''Adds a sale to the sales tables'''
    event_id = int(input("Enter event id: "))
    product_id = int(input("Enter product id: "))
    amount_sold = int(input("# Sold: "))
    db.add_sale(event_id, product_id, amount_sold)
    message("Sale Added")

def edit_sale():
    '''Edits a sale'''
    sale_id = int(input("Enter sale id: "))
    amount_sold = int(input("New # Sold: "))
    db.update_sale(sale_id, amount_sold)
    message("Sale Edited")

def delete_sale():
    '''Deltes a sale'''
    sale_id = int(input("Enter sale id: "))
    sale = db.get_sale_by_id(sale_id)
    db.remove_sale(sale_id)
    message("Sale Deleted")

def message(msg):
    '''Display a message to the user'''
    print(msg)