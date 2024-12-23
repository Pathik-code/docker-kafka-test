from flask import Flask, jsonify
import json
import threading
import time
import random

app = Flask(__name__)

# Data that will be served
data = []

def update_data():
    """Function to update the data list with random values every 1 minute."""
    global data
    while True:
        # Generate new random data
        new_data = [{'key': f'value_{i}', 'index': i, 'random_value': random.randint(1, 100)} for i in range(10)]
        data = new_data
        print("Data updated:", data)  # Optional: log the updated data
        time.sleep(60)  # Wait for 1 minute

@app.route('/data', methods=['GET'])
def get_data():
    """Endpoint to return the data in JSON format."""
    return jsonify(data)

# Start the server on port 9092
if __name__ == '__main__':
    # Start the data updater thread
    updater_thread = threading.Thread(target=update_data, daemon=True)
    updater_thread.start()
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=9092)
