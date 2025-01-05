from flask import Flask, jsonify

app = Flask(__name__)

# sample data
items = [
    {'id': 1, 'name': 'chocolates', 'price': 100},
    {'id': 2, 'name': 'cake', 'price': 250},
    {'id': 3, 'name': 'candles', 'price': 50},
]

# Home route
@app.route('/')
def home():
    return "Welcome to BIRTHDAY API!"

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

# GET a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

# POST a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = {'id': 4, 'name': 'dress', 'price': 300}
    items.append(new_item)
    return jsonify(new_item)

# PUT to update an existing item
@app.route('/items', methods=['PUT'])
def update_item():
    items[2]['name']='birthday cake'
    return jsonify(items)


# PATCH to partially update an existing item
@app.route('/items/<int:item_id>', methods=['PATCH'])
def patch_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    data = {
        'name': 'updated name',
        'price': 150
    }
    if 'name' in data:
        item['name'] = data['name']
    if 'price' in data:
        item['price'] = data['price']

    return jsonify(item)

# DELETE an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': f'Item with id {item_id} deleted'}), 200

if __name__ == '__main__':
    app.run(port=3003)
