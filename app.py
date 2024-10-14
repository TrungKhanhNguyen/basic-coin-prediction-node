from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/inference/<token>', methods=['GET'])
def get_inference(token):
    file_path = f'data/{token}.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read().strip()  # Read and strip any leading/trailing whitespace
            try:
                price = float(data)  # Convert string data to float
                adjustment_factor = random.uniform(0.99, 1.01)
                adjusted_price = price * adjustment_factor
                if token == 'ARB':
                    return str(format(adjusted_price, ".4f"))
                else:
                    return str(format(adjusted_price, ".2f"))
            except ValueError:
                return jsonify({"error": "Invalid data in file"}), 500
    else:
        return jsonify({"error": "Token data not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011)
