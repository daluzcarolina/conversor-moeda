from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Substitua com sua API Key
API_KEY = "s089278a6e675a8d0a9d7a32b"
API_URL = f"https://v6.exchangerate-api.com/v6/089278a6e675a8d0a9d7a32b/latest/USD"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        
        response = requests.get(API_URL)
        data = response.json()
        
        # Obtenha a taxa de câmbio para as moedas
        from_rate = data['conversion_rates'][from_currency]
        to_rate = data['conversion_rates'][to_currency]
        
        # Converta o valor
        converted_amount = (amount / from_rate) * to_rate
        
        return jsonify({'result': round(converted_amount, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
