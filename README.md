# MQTT-RabbitMQ-MongoDB Integration Project

## Overview

This project demonstrates a client-server architecture where MQTT messages are published via RabbitMQ, processed by a server, and stored in MongoDB. Additionally, a Flask API provides an endpoint to retrieve counts of different status values within a specified time range.

## Project Structure
.
├── client.py # Script to generate and publish MQTT messages
├── server.py # Server script to process messages and store them in MongoDB
├── app.py # Flask API for data retrieval
├── requirements.txt # List of required Python packages
└── tests/ # Directory for unit and integration tests


## Prerequisites
Before you begin, ensure you have the following installed:

- **Python 3.x**
- **RabbitMQ**: [Download and Install RabbitMQ](https://www.rabbitmq.com/download.html)
- **MongoDB**: [Download and Install MongoDB](https://www.mongodb.com/try/download/community)


Setup Instructions:
-------------------
1. Clone the Repository
   git clone <repository-url>
   cd <repository-directory>

2. Create and Activate a Virtual Environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Start RabbitMQ and MongoDB
Ensure that both RabbitMQ and MongoDB are running on their default ports:

RabbitMQ should be accessible at localhost:5672.
MongoDB should be accessible at mongodb://localhost:27017/.

5. Run the MQTT Client Script
   python client.py

6. Run the Server Script
   python server.py

7. Run the Flask API
   python app.py

Using the API
Endpoint
URL: /status_count
Method: GET
Parameters:
start_time: ISO 8601 formatted datetime string (e.g., 2023-01-01T00:00:00)
end_time: ISO 8601 formatted datetime string (e.g., 2023-01-01T01:00:00)


Example Request:
----------------
curl "http://localhost:5000/status_count?start_time=2023-01-01T00:00:00&end_time=2023-01-01T01:00:00"


Example Response: 
-----------------
{
  "0": 10,
  "1": 12,
  "2": 9,
  "3": 14,
  "4": 8,
  "5": 11,
  "6": 13
}


Testing:
--------
Running Tests
   pytest tests/

Test Structure
The tests are located in the tests/ directory and include unit and integration tests for the MQTT client, server, and API.


Troubleshooting:
----------------
Common Issues:
RabbitMQ Connection Error: Ensure RabbitMQ is running and accessible on localhost:5672.
MongoDB Connection Error: Ensure MongoDB is running and accessible on mongodb://localhost:27017/.
Flask API Not Responding: Check if the Flask server is running on the correct port (5000 by default).


Logs and Debugging:
-------------------
The MQTT client and server scripts print log messages to the console for monitoring.
Flask API logs requests and errors in the console.


License:
--------
This project is licensed under the MIT License.