from flask import Flask, url_for, request, json, jsonify
from product import Product
from customer import Customer
from sales import Sales
from json import dumps


app = Flask(__name__)
products = []
customers = []
my_sales = []


@app.route('/customers/feed')
def api_feed_customer():
    customers.append(Customer(1, "Ignis"))
    customers.append(Customer(2, "Arier"))
    customers.append(Customer(3, "Noctis"))
    customers.append(Customer(4, "Claire"))
    customers.append(Customer(5, "Ookami"))
    customers.append(Customer(6, "Amaterasu"))
    json_aux = {'status': 'alimentado'}
    return jsonify(json_aux), 200


@app.route('/products/feed')
def api_feed_product():
    products.append(Product(1, "FINAL FANTASY XV ROYAL EDITION", 102.90))
    products.append(Product(2, "NieR: Automata™ Game of the YoRHa Edition", 133.66))
    products.append(Product(3, "Sekiro: Shadows Die Twice", 224.91))
    products.append(Product(4, "Devil May Cry 5", 179.90))
    products.append(Product(5, "Star Wars: The Old Republic", 65.10))
    products.append(Product(6, "Dark Souls III The Fire Fades Edition", 116.91))
    json_aux = {'status': 'alimentado'}
    return jsonify(json_aux), 200


@app.route('/sales/feed')
def api_feed_sales():
    my_sales.append(Sales(1, 1, 1))
    my_sales.append(Sales(2, 6, 6))
    my_sales.append(Sales(3, 3, 2))
    my_sales.append(Sales(4, 1, 2))
    my_sales.append(Sales(5, 4, 1))
    my_sales.append(Sales(6, 4, 3))
    my_sales.append(Sales(7, 3, 6))
    my_sales.append(Sales(8, 3, 5))
    my_sales.append(Sales(9, 5, 4))
    json_aux = {'status': 'alimentado'}
    return jsonify(json_aux), 200

@app.route('/customers', methods=['POST'])
def api_create_customer():
    # pega o json do corpo da requição
    req_data = request.get_json()

    # pega o id e o nome do json da requisição
    id = req_data['id']
    name = req_data['name']

    # cria um novo customer baseado no id e nome que veio do json
    new_customer = Customer(id, name)

    # adiciona o novo customer no array global de customers
    customers.append(new_customer)

    json_aux = {'status': 'criado'}
    return jsonify(json_aux), 201


@app.route('/customers', methods=['GET'])
def api_get_all_customers():
    all_customers = []

    for customer in customers:
        json_aux = {
            'id': customer.get_id(),
            'nome': customer.get_name()
        }
        all_customers.append(json_aux)

    return jsonify(all_customers), 200


@app.route('/customers/<id>', methods=['GET'])
def api_get_customer_by_id(id):
    json_aux = None

    for customer in customers:
        customer_id = customer.get_id()
        if(int(id) == int(customer_id)):
            json_aux = {
                'id': customer_id,
                'nome': customer.get_name()
            }
            break

    if json_aux == None:
        json_aux = {'status': 'cliente nao encontrado'}
        return jsonify(json_aux), 404

    return jsonify(json_aux), 200


@app.route('/customers/<id>/sales', methods=['GET'])
def api_get_customer_sales_by_customer_id(id):
    json_aux = None
    customer_id = id
    # Get all sales where customer_id match id
    customer_sales = []
    for sale in my_sales:
        sale_customer_id = int(sale.get_customer_id())

        if(int(customer_id) == sale_customer_id):
            sale_product_id = sale.get_product_id()

            # get product by sale_product_id
            for product in products:
                if (int(product.get_id()) == int(sale_product_id)):
                    json_aux = True
                    new_customer_sale = {
                        'id': product.get_id(),
                        'nome': product.get_description(),
                        'price': product.get_price()
                    }
                    customer_sales.append(new_customer_sale)
                    break

    if json_aux == None:
        json_aux = {'status': 'cliente nao possui compras'}
        return jsonify(json_aux), 404

    return jsonify(customer_sales), 200


# products

# POST /products
@app.route('/products', methods=['POST'])
def api_create_product():
    req_data = request.get_json()

    id = req_data['id']
    description = req_data['description']
    price = req_data['price']

    new_product = Product(id, description, price)

    products.append(new_product)

    json_aux = {'status': 'Created'}
    return jsonify(json_aux), 201


# GET /products
@app.route('/products', methods=['GET'])
def api_get_all_products():
    all_products = []

    for product in products:
        aux = {
            'id': product.get_id(),
            'descricao': product.get_description(),
            'price': product.get_price()
        }
        all_products.append(aux)

    return jsonify(all_products), 200


# GET /products/<id>
@app.route('/products/<id>', methods=['GET'])
def api_get_product_by_id(id):
    json_aux = None

    for product in products:
        aux_id = product.get_id()
        if(int(id) == int(aux_id)):
            json_aux = {
                'id': product.get_id(),
                'descricao': product.get_description(),
                'price': product.get_price()
            }
            break

    if json_aux == None:
        json_aux = {'status': 'produto nao encontrado'}
        return jsonify(json_aux), 404

    return jsonify(json_aux), 200

# sales

# POST /sales
@app.route('/sales', methods=['POST'])
def api_create_sale():
    req_data = request.get_json()

    id = req_data['id']
    costumer_id = req_data['costumer_id']
    product_id = req_data['product_id']

    new_sale = Sales(id, costumer_id, product_id)

    my_sales.append(new_sale)

    json_aux = {'status': 'criado'}
    return jsonify(json_aux), 201


# GET /sales
@app.route('/sales', methods=['GET'])
def api_get_all_sales():
    all_sales = []

    for sale in my_sales:
        json_aux = {
            'id': sale.get_id(),
            'id_do_cliente': sale.get_customer_id(),
            'id_do_produto': sale.get_product_id()
        }
        all_sales.append(json_aux)

    return jsonify(all_sales), 200


# GET /sales/<id>
@app.route('/sales/<id>', methods=['GET'])
def api_get_sales_by_id(id):
    json_aux = None

    for sale in my_sales:
        aux_id = sale.get_id()
        if(int(id) == int(aux_id)):
            json_aux = {
                'id': sale.get_id(),
                'id_do_cliente': sale.get_customer_id(),
                'id_do_produto': sale.get_product_id()
            }
            break

    if json_aux == None:
        json_aux = {'status': 'venda nao encontrada'}
        return jsonify(json_aux), 404

    return jsonify(json_aux), 200


if __name__ == '__main__':
    app.run()
