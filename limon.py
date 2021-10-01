import csv
def read():
    data = []
    with open('bd/products.csv','r', encoding='utf-8') as products_file:
        products = csv.reader(products_file)
        header = next(products)
        for row in products:
            product ={ h: r for h, r in zip(header, row)}
            data.append(product)
    return data
def append_product(product_name, price):
    DATA = [product_name.lower(), price]
    with open('bd/products.csv','a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(DATA)
def not_exist_product(name):
    DATA = read()
    if not any(d.get('name').lower() == name.lower() for d in DATA): # Modificar linea de codigo.
        return True
    return False

def get_price(name):
    DATA = read()
    price =  [d['price'] for d in DATA if d['name'].lower() == name.lower()]
    return price[0]

def run():
        product_name = input('>')
        if len(product_name) > 0 and not any(chr.isdigit() for chr in product_name):
            if  not_exist_product(product_name):
                product_price = input('$ ')
                append_product(product_name, product_price)
            else:
                print("$ " + get_price(product_name))


if __name__ == '__main__':
    try:
        while True:
            run()
    except KeyboardInterrupt:
        pass
