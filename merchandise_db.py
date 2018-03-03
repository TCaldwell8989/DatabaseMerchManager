import sqlite3

# Renaissance database setup and management
conn = sqlite3.connect('renaissance.db')

c = conn.cursor()

# Enforces Foreign Key Relationships
c.execute("PRAGMA foreign_keys = 1")

# Create products table, events table, and sales table
c.execute("""CREATE TABLE IF NOT EXISTS products (
          id INTEGER NOT NULL PRIMARY KEY, product_name TEXT, price REAL, quantity INTEGER , description TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS events (
          id INTEGER NOT NULL PRIMARY KEY, event_name TEXT, event_date TEXT, location TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS sales (
          id INTEGER NOT NULL PRIMARY KEY, event_id INTEGER, product_id INTEGER, amount_sold INTEGER,
          FOREIGN KEY(event_id) REFERENCES events(id),
          FOREIGN KEY(product_id) REFERENCES products(id))""")


# Product Table Methods
def insert_product(product):
    with conn:
        c.execute("INSERT INTO products VALUES (null, :product_name, :price, :quantity, :description)",
            {'product_name': product.name, 'price': product.price,
             'quantity': product.quantity, 'description': product.description})

def get_products():
    c.execute("SELECT * FROM products")
    return c.fetchall()

def get_product_by_id(product_id):
        c.execute("SELECT * FROM products WHERE id = :product_id", {'product_id': product_id})
        return c.fetchone()

def update_price(product_id, price):
    with conn:
        c.execute("""UPDATE products SET price = :price WHERE id = :product_id""",
                  {'product_id': product_id, 'price': price})

def update_quantity(product_id, quantity):
    with conn:
        c.execute("""UPDATE products SET quantity = :quantity WHERE id = :product_id""",
                  {'product_id': product_id, 'quantity': quantity})

def remove_product(product_id):
    with conn:
        c.execute("""DELETE FROM products WHERE id = :product_id""",
                  {'product_id': product_id})


# EVENT TABLE METHODS
def insert_event(event):
    with conn:
        c.execute("INSERT INTO events VALUES (null, :event_name, :event_date, :location)",
            {'event_name': event.name, 'event_date': event.date, 'location': event.location})

        #c.execute("INSERT INTO events VALUES (?, ?, ?)",
        #          (event.name, event.date, event.location))

def get_events():
    c.execute("SELECT * FROM events")
    return c.fetchall()


def get_event_by_id(event_id):
    c.execute("SELECT * FROM events WHERE id = :event_id", {'event_id': event_id})
    return c.fetchone()


def get_events_by_name(event_name):
        c.execute("SELECT * FROM events WHERE event_name = :event_name", {'event_name': event_name})
        return c.fetchall()

def update_event_date(event_id, event_date):
    with conn:
        c.execute("""UPDATE events SET event_date = :event_date WHERE id = :event_id""",
                  {'event_id': event_id, 'event_date': event_date})

def update_location(event_id, location):
    with conn:
        c.execute("""UPDATE events SET location = :location WHERE id = :event_id""",
                  {'event_id': event_id, 'location': location})

def remove_event(event_id):
    with conn:
        c.execute("""DELETE FROM events WHERE id = :event_id""",
                  {'event_id': event_id})


# Sales Table Methods
def add_sale(event_id, product_id, amount):
    with conn:
        c.execute("INSERT INTO sales VALUES (null, :event_id, :product_id, :amount)",
            {'event_id': event_id, 'product_id': product_id, 'amount': amount})

def get_sales():
    c.execute("SELECT * FROM sales")
    return c.fetchall()

def get_sale_by_id(sale_id):
    c.execute("SELECT * FROM sales WHERE id = :sale_id", {'sale_id': sale_id})
    return c.fetchone()

def get_sales_by_event(event_id):
    c.execute("SELECT * FROM sales WHERE event_id = :event_id", {'event_id': event_id})
    return c.fetchall()

def get_sales_by_product(product_id):
    c.execute("SELECT * FROM sales WHERE product_id = :product_id", {"product_id": product_id})

def update_sale(sale_id, new_amount):
    c.execute("UPDATE sales SET amount_sold = :amount_sold WHERE id = :sale_id",
              {'sale_id': sale_id, 'amount_sold': new_amount})

def remove_sale(sale_id):
    with conn:
        c.execute("DELETE FROM sales WHERE id = :sale_id",
                  {'sale_id': sale_id})


# Aggregate queries return results
def most_sold_product():
    c.execute("SELECT product_id, SUM(amount_sold) FROM sales GROUP BY product_id")
    return c.fetchall()

def festival_sold_most_crystals():
    c.execute("SELECT event_id, SUM(amount_sold) FROM sales GROUP BY event_id")
    return c.fetchall()

