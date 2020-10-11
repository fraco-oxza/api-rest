from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from products import productos

@app.route("/")
def home():
    print("alguien entro")
    return render_template("index.html")

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/products")
def getProducts():
    return jsonify(productos)

@app.route("/products/<string:product_name>")
def getProduct(product_name):
    product_found = [product for product in productos if product["name"] == product_name]
    if len(product_found) > 0:
        return jsonify({"product" : product_found[0]})
    return jsonify({"message" : "product not found"}) 

@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name"  : request.json["name"],
        "price" : request.json["price"],
        "items" : request.json["items"]
    }
    productos.append(new_product)
    return jsonify({"message" : "Done", "products": productos})

@app.route("/products/<name_product>", methods=["PUT"])
def editProducts(name_product):
    product_found = [product for product in productos if product["name"] == name_product]

    if (len(product_found) > 0):
        product_found[0]["name"]   = request.json["name"]
        product_found[0]["price"]  = request.json["price"]
        product_found[0]["items"]  = request.json["items"]
        return jsonify({"message": "Product update", "product": product_found[0]})
    return jsonify({"message": "error no se a encontrado el producto"})

@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProducts(product_name):
    product_found = [product for product in productos if product["name"] == product_name]
    if len(product_found) > 0:
        productos.remove(product_found [0])
        return jsonify({"message": "10:4"})
    return jsonify({"message": "el producto no se a encontrado"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)