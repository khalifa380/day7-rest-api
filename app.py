from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
items = [
    {"id": 1, "name": "Pen", "price": 10},
    {"id": 2, "name": "Notebook", "price": 25}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Day 7 Mini Project - REST API"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    return jsonify(item) if item else jsonify({"error": "Item not found"}), 404

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        data = request.get_json()
        item.update(data)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
