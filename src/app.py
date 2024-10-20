from flask import Flask, jsonify, request



app = Flask(__name__)
todos = [{"label": "My first task", "done": True}]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
     
    return jsonify(todos)









#No mover estas dos líneas:

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)