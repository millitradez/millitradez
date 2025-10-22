<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #101820; color: #fff; text-align: center; }
        .container { max-width: 700px; margin: 50px auto; padding: 20px; background: #1b2735; border-radius: 10px; }
        input[type=text] { width: 80%; padding: 10px; border: none; border-radius: 5px; margin: 10px 0; }
        button { background: #00c896; border: none; padding: 10px 20px; color: #fff; border-radius: 5px; cursor: pointer; }
        .balance, .tokens, .trades { margin-top: 20px; text-align: left; }
        table { width: 100%; border-collapse: collapse; color: #ddd; }
        th, td { padding: 10px; border-bottom: 1px solid #333; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Wallet Dashboard</h2>
        <form action="/wallet" method="post">
            <input type="text" name="wallet_address" placeholder="Enter your Solana wallet address" required>
            <br>
            <button type="submit">View Wallet</button>
        </form>

        {% if wallet_data %}
            <div class="balance">
                <h3>Wallet: {{ wallet_data.address }}</h3>
                <p><strong>SOL Balance:</strong> {{ wallet_data.sol_balance }}</p>
            </div>

            <div class="tokens">
                <h3>Tokens</h3>
                <table>
                    <tr><th>Token</th><th>Symbol</th><th>Balance</th></tr>
                    {% for token in wallet_data.tokens %}
                        <tr><td>{{ token.name }}</td><td>{{ token.symbol }}</td><td>{{ token.balance }}</td></tr>
                    {% endfor %}
                </table>
            </div>

            <div class="trades">
                <h3>Recent Trades</h3>
                <table>
                    <tr><th>Pair</th><th>Action</th><th>Amount</th><th>Price</th></tr>
                    {% for trade in trades %}
                        <tr>
                            <td>{{ trade.pair }}</td>
                            <td>{{ trade.action }}</td>
                            <td>{{ trade.amount }}</td>
                            <td>{{ trade.price }}</td>
                        </tr>
                    {% endfor %}
                </table>
            </div>
        {% endif %}
    </div>
</body>
</html>

