# https://github.com/jhnwr/shopify-product-check
import csv

from dotenv import load_dotenv

from db.database import create_db_and_tables
from services.email_service import send_mail
from services.scraper import extract, transform, add_products


def configure():
    load_dotenv()


def stores_list():
    with open('storelist.csv', 'r') as f:
        reader = csv.reader(f, skipinitialspace=True)
        stores = list(map(tuple, reader))
    return stores


def update():
    new_items = []
    for store in stores_list():
        print(f'Adding from Store: {store}')
        output = extract(store[1])
        formatted = transform(store[0], output)
        new_items.append(add_products(formatted))
    only_new = [item for sl in new_items for item in sl]
    return only_new


def alert(new):
    send_mail(new)
    pass


def main():
    create_db_and_tables()
    configure()
    ni = update()
    alert(ni)


if __name__ == '__main__':
    main()
