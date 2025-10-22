from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/trade', methods=['GET', 'POST']) def trade():
    if request.method == 'POST':
        pair = request.form['pair']
        amount = request.form['amount']
        contract_address = request.form['contract_address']

        message = f"Trading {amount} of {pair} using contract {contract_address}."
        return render_template("trade.html", message=message)

    return render_template("trade.html")

if __name__ == "__main__":
    app.run(debug=True)
