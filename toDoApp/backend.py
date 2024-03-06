 
# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

todo_list = []

@app.route('/api/add', methods=['POST'])
def add_todo():
    todo_item = request.json.get('todo_item')
    todo_list.append(todo_item)
    return jsonify({"message": "Todo item added successfully"}), 201

@app.route('/api/remove', methods=['POST'])
def remove_todo():
    index = request.json.get('index')
    del todo_list[index]
    return jsonify({"message": "Todo item removed successfully"}), 200

@app.route('/api/list', methods=['GET'])
def get_todo_list():
    return jsonify(todo_list), 200

if __name__ == '__main__':
    app.run(debug=True)
