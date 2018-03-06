import os
import unittest
import sqlite3
import merchandise_db as database
from product import Product
from event import Event

class TestMerchDB(unittest.TestCase):

    test_db_file = "test.db"

    def setUp(self):
        database.db_path = self.test_db_file
        database.create_database()

    def test_add_new_product(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        database.insert_product(product1)
        db_products = database.get_products()
        self.assertEqual(1, len(db_products))

    def test_add_new_event(self):
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_event(event1)
        db_events = database.get_events()
        self.assertEqual(1, len(db_events))

    def test_add_new_sale(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_product(product1)
        database.insert_event(event1)
        database.add_sale(1, 1, 5)
        db_sales = database.get_sales()
        self.assertEqual(1, len(db_sales))

    def test_remove_product(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        database.insert_product(product1)
        database.remove_product(1)
        self.assertEqual(0, len(database.get_products()))

    def test_remove_event(self):
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_event(event1)
        database.remove_event(1)
        self.assertEqual(0, len(database.get_events()))

    def test_remove_sale(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_product(product1)
        database.insert_event(event1)
        database.add_sale(1, 1, 5)
        database.remove_sale(1)
        self.assertEqual(0, len(database.get_sales()))

    def test_update_product_price(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        database.insert_product(product1)
        new_price = 34.99
        database.update_price(1, new_price)
        db_product = database.get_product_by_id(1)
        self.assertEqual(new_price, db_product[2])

    def test_update_event_date_failure(self):
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_event(event1)
        new_date = "Wrong format"
        self.assertRaises(ValueError, database.update_event_date(1, new_date))

    def test_add_sale_where_product_id_failure(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_product(product1)
        database.insert_event(event1)
        self.assertRaises(sqlite3.IntegrityError, database.add_sale(1, 2, 5))

    def test_add_sale_where_quantity_failure(self):
        product1 = Product("Crystals", 24.99, 10, "Small clear crystals")
        event1 = Event("MN Renaissance Festival", "08/09/2018", "Shakopee, MN")
        database.insert_product(product1)
        database.insert_event(event1)
        self.assertRaises(ValueError, database.add_sale(1, 1, 15))

    def tearDown(self):
        os.remove(self.test_db_file)
