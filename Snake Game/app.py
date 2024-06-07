from flask import Flask, render_template, request, jsonify
import random
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://s26816:xui228@snake.ovqb4xa.mongodb.net/?retryWrites=true&w=majority&appName=Snake")
db = client["Snake"]
collection = db["scores"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    nickname = request.form.get('nickname')
    board_size = int(request.form.get('board_size'))
    return render_template('game.html', nickname=nickname, board_size=board_size)

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    nickname = data['nickname']
    score = data['score']
    board_size = data['board_size']
    collection.insert_one({"nickname": nickname, "score": score, "board_size": board_size})
    return jsonify({"status": "success"})

@app.route('/high_scores')
def high_scores():
    scores = list(collection.find().sort("score", -1).limit(10))
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
