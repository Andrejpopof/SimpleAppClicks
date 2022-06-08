from crypt import methods
import os
from datetime import datetime
from flask import Flask, jsonify, url_for
from flask_cors import cross_origin
from pymongo import MongoClient



app = Flask(__name__)


username = os.environ["MONGODB_USER"]
password = os.environ["MONGODB_PASSWORD"]
host = os.environ["MONGODB_HOST"] 
portDB = os.environ["MONGODB_PORT"]
portBE = os.environ["BACKEND_PORT"]
dbName = os.environ["MONGODB_NAME"]


client = MongoClient(
    "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (username, password, host,portDB,dbName)
)  


db = client.dbName
collection = db["hits"] 


@app.route("/", methods=["GET"])
@cross_origin()
def root():
    collection.insert_one({"time": datetime.utcnow()})
    message = "This page has been visited {} times.".format(collection.count())
    return jsonify({"message": message})

# @app.route("/hello")
# def hello():
#     return url_for("root")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=portBE)
