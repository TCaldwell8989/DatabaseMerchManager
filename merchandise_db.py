import sqlite3
import logging as log

log.basicConfig(filename='MerchDB.log',level=log.INFO)

db_path = "renaissance.db"

# Renaissance database setup and management
def create_database():
    conn = sqlite3.connect(db_path)
    log.info("Connected to database")
    c = conn.cursor()

    # Enforces Foreign Key Relationships
    c.execute("PRAGMA foreign_keys = 1")

    # Table setup
    c.execute("""CREATE TABLE IF NOT EXISTS products (
              id INTEGER NOT NULL PRIMARY KEY, product_name TEXT, price REAL, quantity INTEGER , description TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS events (
              id INTEGER NOT NULL PRIMARY KEY, event_name TEXT, event_date TEXT, location TEXT)""")

    c.execute("""CREATE TABLE IF NOT EXISTS sales (
              id INTEGER NOT NULL PRIMARY KEY, event_id INTEGER, product_id INTEGER, amount_sold INTEGER,
              FOREIGN KEY(event_id) REFERENCES events(id),
              FOREIGN KEY(product_id) REFERENCES products(id))""")
    log.info("Created tables")


# PRODUCT TABLE METHODS
def insert_product(product):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("INSERT INTO products VALUES (null, :product_name, :price, :quantity, :description)",
            {'product_name': product.name, 'price': product.price,
             'quantity': product.quantity, 'description': product.description})
        db.commit()
        log.info("product added")

def get_products():
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM products")
        return c.fetchall()

def get_product_by_id(product_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM products WHERE id = :product_id", {'product_id': product_id})
        return c.fetchone()

def update_price(product_id, price):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""UPDATE products SET price = :price WHERE id = :product_id""",
                  {'product_id': product_id, 'price': price})
        db.commit()
        log.info("Price updated")

def update_quantity(product_id, quantity):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""UPDATE products SET quantity = :quantity WHERE id = :product_id""",
                  {'product_id': product_id, 'quantity': quantity})
        db.commit()
        log.info("Quantity updated")

def remove_product(product_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""DELETE FROM products WHERE id = :product_id""",
                  {'product_id': product_id})
        db.commit()
        log.info("Product deleted")


# EVENT TABLE METHODS
def insert_event(event):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("INSERT INTO events VALUES (null, :event_name, :event_date, :location)",
            {'event_name': event.name, 'event_date': event.date, 'location': event.location})

        #c.execute("INSERT INTO events VALUES (?, ?, ?)",
        #          (event.name, event.date, event.location))

        db.commit()
        log.info("Event added")

def get_events():
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM events")
        return c.fetchall()

def get_event_by_id(event_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM events WHERE id = :event_id", {'event_id': event_id})
        return c.fetchone()


def get_events_by_name(event_name):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM events WHERE event_name = :event_name", {'event_name': event_name})
        return c.fetchall()

def update_event_date(event_id, event_date):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""UPDATE events SET event_date = :event_date WHERE id = :event_id""",
                  {'event_id': event_id, 'event_date': event_date})
        db.commit()
        log.info("Event date updated")

def update_location(event_id, location):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""UPDATE events SET location = :location WHERE id = :event_id""",
                  {'event_id': event_id, 'location': location})
        db.commit()
        log.info("Location updated")

def remove_event(event_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("""DELETE FROM events WHERE id = :event_id""",
                  {'event_id': event_id})
        db.commit()
        log.info("Event removed")


# SALES TABLE METHODS
def add_sale(event_id, product_id, amount):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("INSERT INTO sales VALUES (null, :event_id, :product_id, :amount)",
            {'event_id': event_id, 'product_id': product_id, 'amount': amount})
        db.commit()
        log.info("Sale added")

def get_sales():
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM sales")
        return c.fetchall()

def get_sale_by_id(sale_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM sales WHERE id = :sale_id", {'sale_id': sale_id})
        return c.fetchone()

def get_sales_by_event(event_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM sales WHERE event_id = :event_id", {'event_id': event_id})
        return c.fetchall()

def get_sales_by_product(product_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT * FROM sales WHERE product_id = :product_id", {"product_id": product_id})

def remove_sale(sale_id):
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("DELETE FROM sales WHERE id = :sale_id",
                  {'sale_id': sale_id})
        db.commit()
        log.info("Sale removed")


# Aggregate queries that return results
def most_sold_product():
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT product_id, SUM(amount_sold) FROM sales GROUP BY product_id")
        return c.fetchall()

def festival_sold_most_crystals():
    with sqlite3.connect(db_path) as db:
        c = db.cursor()
        c.execute("SELECT event_id, SUM(amount_sold) FROM sales GROUP BY event_id")
        return c.fetchall()

