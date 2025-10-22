from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/trade', methods=['GET', 'POST']) def trade():
    if request.method == 'POST':
        pair = request.form.get('pair')
        amount = request.form.get('amount')
        contract_address = request.form.get('contract_address')

        # You can add your trading logic here later
        message = f"Trade executed: {amount} {pair} (Contract: {contract_address})"
        return render_template('trade.html', message=message)

    return render_template('trade.html')

if __name__ == '__main__':
    app.run(debug=True)
