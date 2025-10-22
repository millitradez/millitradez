from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ---------- ROUTES ----------

@app.route('/')
def wallet():
    # Example wallet data (you can replace this with real blockchain data later)
    wallet_data = {
        "address": "0x1234...ABCD",
        "balance": "2.5 ETH",
        "network": "Ethereum Mainnet"
    }
    return render_template('wallet.html', wallet=wallet_data)

@app.route('/api/wallet')
def get_wallet_data():
    # Same wallet info returned as JSON (for dynamic use with JavaScript)
    wallet_data = {
        "address": "0x1234...ABCD",
        "balance": "2.5 ETH",
        "network": "Ethereum Mainnet"
    }
    return jsonify(wallet_data)


# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)


      
