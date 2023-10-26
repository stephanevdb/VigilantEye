from flask import Flask, render_template, request, redirect, url_for
from modules.ping import ping4, ping6

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    target = request.form.get('target')
    ping_en = request.form.get('ping')
    
    # Process the form data as needed
    # For this example, we'll just print the data
    print(f"Target: {target}")
    print(f"Ping: {ping_en}")
    ping4(target)
    ping6(target)

    # You can redirect to another page or return a response as needed
    return redirect(url_for('index'))
    

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/test")
def test():
    return render_template('test.html'), 200

@app.route("/output")
def output():
    return render_template('output.html')

if __name__ == "__main__":
    app.run(debug=True)
