
from flask import Flask, jsonify
import os
import random
app = Flask(__name__)

app_base_path = os.getenv("APP_BASE_PATH", default=os.getcwd())
data_base_path = os.path.join(app_base_path, "inference-data")

@app.route('/inference/<token>', methods=['GET'])
def get_price(token):
    try:
        file_name = os.path.join(data_base_path, f'{token.upper()}.txt')
        with open(file_name, 'r') as file:
            data = file.read()
            price = float(data)  # Convert string data to float
            adjustment_factor = random.uniform(0.995, 1.005)
            adjusted_price = price * adjustment_factor
            if token == 'ARB':
                return str(format(adjusted_price, ".4f"))
            else:
                return str(format(adjusted_price, ".2f"))
        #return jsonify({token: data})
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011)
