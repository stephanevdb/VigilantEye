from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/test")
def test():
    return render_template('test.html'), 200

if __name__ == "__main__":
    app.run(debug=True)
