from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_score(self, nickname, score, board_size):
        self.collection.insert_one({"nickname": nickname, "score": score, "board_size": board_size})

    def get_high_scores(self):
        return list(self.collection.find().sort("score", -1))