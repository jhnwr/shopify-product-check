import requests
from sqlmodel import Session, select

from db.database import engine
from db.models import Product


def extract(store):
    results = []

    def pages(page):
        # view source and search for '.myshopify.com' for main URL
        url = store + f'/products.json?limit=250&page={page}'
        r = requests.get(url)
        if r.status_code != 200:
            r.raise_for_status()
        resp = r.json()
        return resp['products']

    x = 1
    out = pages(x)
    results.append(out)

    if len(out) == 250:
        while True:
            extra = pages(x + 1)
            if len(extra) == 0:
                break
            results.append(extra)
            x += 1

    combined = [item for sl in results for item in sl]
    return combined


def transform(store, data):
    formatted_data = []
    for product in data:
        formatted_data.append(
            (store, product['id'], product['title'], product['published_at'], product['handle'])
        )
    return formatted_data


def add_products(json_data):
    new_items = []
    with Session(engine) as session:
        for item in json_data:
            p_load = Product(
                store_id=item[1],
                store_name=item[0],
                title=item[2],
                handle=item[4],
                published=item[3],
            )
            statement = select(Product).where(Product.title == item[2])
            res = session.exec(statement)
            if not res.first():
                session.add(p_load)
                session.commit()
                session.refresh(p_load)
                print(f'added product {item}')
                new_items.append(item)
    return new_items


if __name__ == '__main__':
    store = ('allbirds', 'https://www.allbirds.co.uk')
    output = extract(store[1])
    formatted = transform(store[0], output)
    print(formatted)
