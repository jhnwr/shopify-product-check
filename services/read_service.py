import csv
from typing import List

from sqlmodel import Session, select, SQLModel

from db.database import engine
from db.models import Product


def get_all() -> List:
    output = []
    with Session(engine) as session:
        statement = select(Product)
        res = session.exec(statement)
        for pr in res:
            product_dict = {
                'store_name': pr.store_name,
                'title': pr.title,
                'handle': pr.handle,
                'published': pr.published,
            }
            output.append(product_dict)
    # print(output)
    return output


def to_csv(output):
    keys = output[0].keys()

    with open('dump.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(output)