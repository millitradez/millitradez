from flask import Flask, render _template
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('wallet.html')
    @app.route('/trade')
    def trade():
        return render_templates('trade.html')
        if __name__ '__main__':
        app.run(debug=True)
