from flask import Flask, request, jsonify
import pymongo
from datetime import datetime

app = Flask(__name__)

# MongoDB settings
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'mqtt_data'
MONGO_COLLECTION = 'status_updates'

# Initialize MongoDB client
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

@app.route('/status_count', methods=['GET'])
def get_status_count():
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')

        if not start_time or not end_time:
            return jsonify({"error": "Please provide start_time and end_time"}), 400

        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)

        pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ]

        result = list(collection.aggregate(pipeline))

        response = {str(doc['_id']): doc['count'] for doc in result}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
