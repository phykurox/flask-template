""" Wrapper class for PyMongo object
Read tutorial @ https://api.mongodb.com/python/current/tutorial.html
"""
from pymongo import MongoClient
from typing import List, Dict, Any
from bson.objectid import ObjectId
from app.helper.config import MongoConfig


class MongoHandler:
    def __init__(self):
        self._db_name = MongoConfig.DB_NAME
        self._collection_name = MongoConfig.DB_COLLECTION_NAME

    def connect(self) -> None:
        endpoint = MongoConfig.DB_CONNECTION_STRING
        self._client = MongoClient(endpoint, connect=False)
        self._db = self._client[self._db_name]
        self._collection = self._db[self._collection_name]

    def insert_one(self, post: Dict) -> str:
        return str(self._collection.insert_one(post).inserted_id)

    def insert_many(self, posts: List) -> List:
        return [str(_id) for _id in
                self._collection.insert_many(posts).inserted_ids]

    def find_by_id(self, _id: str or int) -> Dict:
        try:
            _id = ObjectId(_id)
        except Exception:
            pass
        finally:
            return self.find_one({'_id': _id})

    def find_one(self, query: Dict) -> Dict:
        """ Find the first match """
        doc = self._collection.find_one(query)
        # convert ObjectId to string
        doc and doc.update({'_id': str(doc['_id'])})
        return doc

    def find_many(self, query: Dict = {}) -> Dict:
        """ Find all the matches """
        doc_list = []
        try:
            for doc in self._collection.find(query):
                # convert ObjectId to string
                doc.update({'_id': str(doc['_id'])})
                doc_list.append(doc)
            return doc_list
        except Exception as e:
            raise(e)

    def find_count(self, query: Dict) -> int:
        """ Find the count """
        return self._collection.count_documents(query)

    def delete_one(self, query: Dict) -> None:
        """ Delete the first match """
        return self._collection.delete_one(query)

    def delete_many(self, query: Dict) -> None:
        """ Delete all the matches """
        return self._collection.delete_many(query)

    def drop(self) -> None:
        return self._collection.drop()
