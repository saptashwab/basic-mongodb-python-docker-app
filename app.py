from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['test_database1']
collection = db['items']

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/items', methods=['GET'])
def get_items():
    items = []
    for item in collection.find():
        items.append({'name': item['name'], 'description': item['description']})
    return jsonify({'items': items})

@app.route('/items', methods=['POST'])
def add_item():
    name = request.json['name']
    description = request.json['description']
    item = {'name': name, 'description': description}
    collection.insert_one(item)
    return jsonify({'message': 'Item added successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='9999')