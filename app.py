"""
flask api basic crud
"""

from flask import Flask, jsonify,request
from products import products


app = Flask(__name__)


@app.route('/ping')
def ping():
    """dummy route for test server"""
    return jsonify({"message": "server running"})





@app.route('/products', methods=['GET'])
def get_products():
    """list of all products function"""
    return jsonify({"products": products}, {"message": "all product list"})





@app.route('/products/<int:id>')
def get_product(id):
    """list of an specific product function"""
    products_found = [product for product in products if product['id']==id]
    if len(products_found) > 0:
        return jsonify(products_found)
    return jsonify({'message' : 'product not found'})





@app.route('/products', methods=['POST'])
def add_product():
    """Add new product"""
    new_product = {
        "id" : request.json['id'],
        "name" : request.json['name'],
        "price" : request.json['price'],
        "stock" : request.json['stock'] 
    }
    products.append(new_product)    
    return jsonify({'message': 'Product added succesfully'},{"products": products})





@app.route('/products/<int:id>', methods = ['PUT'])
def update_product(id):
    """update data product"""
    product_found = [product for product in products if product['id'] == id]
    if len(product_found) == 1:
        product_found[0]['name'] = request.json['name']
        product_found[0]['price'] = request.json['price']
        product_found[0]['stock'] = request.json['stock']
        return jsonify({"message": "Product updated", "produt": product_found[0]})
    
    return jsonify({"message": "product not found"})



@app.route('/products/<int:id>', methods = ['DELETE'])
def delete_product(id):
    """Delete product"""
    product_found = [product for product in products if product['id'] == id]
    if len(product_found) == 1:
        products.remove(product_found[0])
        return jsonify({"message": "Product deleted", "Products" : products})

    return jsonify({"message": "product not found"})


          

    return jsonify({"message": "Product not found"})
if __name__ == '__main__':
    app.run(debug = True, port=4000)
