from flask import Flask, render_template, request, redirect, url_for
import sqlite3
#from modules.ping import ping4, ping6

app = Flask(__name__)

db = sqlite3.connect('database.db',check_same_thread=False)
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workers(
        id TEXT PRIMARY KEY,
        online INTEGER DEFAULT 0,
        ipv4_capable INTEGER,
        ipv4_address TEXT,
        ipv6_capable INTEGER,
        ipv6_address TEXT
    )
''')
db.commit()




@app.route('/add_worker', methods=['POST'])
def add_worker():
    data = request.data.decode('utf-8')
    worker_id, ipv4_capable, ipv4_address, ipv6_capable, ipv6_address = data.split(',')
    ipv4_capable = int(ipv4_capable == 'True')
    ipv6_capable = int(ipv6_capable == 'True')
    online = 0
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('INSERT INTO workers (id, online, ipv4_capable, ipv4_address, ipv6_capable, ipv6_address) VALUES (?, ?, ?, ?, ?, ?)', (worker_id, online, ipv4_capable, ipv4_address, ipv6_capable, ipv6_address))
    db.commit()
    return 'Worker added successfully'

@app.route('/remove_worker', methods=['GET','POST'])
def remove_worker():
    if request.method == 'POST':
        data = request.form.get('id')
        worker_id = data
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute('DELETE FROM workers WHERE id = ?', (worker_id,))
        db.commit()
        return redirect(url_for('settings'))
    else:
        return 'Method Not Allowed', 405  

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    #target = request.form.get('target')
    #ping_en = request.form.get('ping')
    
    # Process the form data as needed
    # For this example, we'll just print the data
    #print(f"Target: {target}")
    #print(f"Ping: {ping_en}")
    #ping4(target)
    #ping6(target)
    return redirect(url_for('index'))



@app.route("/settings")
def settings():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM workers WHERE online = 1')  # Filter active workers
    rows = cursor.fetchall()
    active_workers = []

    for row in rows:
        active_workers.append({
            'id': row[0],
            'ipv4_capable': row[2],  # Assuming this is the IPv4 capability column
            'ipv4_address': row[3],  # Assuming this is the IPv4 address column
            'ipv6_capable': row[4],  # Assuming this is the IPv6 capability column
            'ipv6_address': row[5]  # Assuming this is the IPv6 address column
        })
    cursor.execute('SELECT * FROM workers WHERE online = 0')  # Filter active workers
    rows = cursor.fetchall()
    dead_workers = []

    for row in rows:
        dead_workers.append({
            'id': row[0],
            'ipv4_capable': row[2],  # Assuming this is the IPv4 capability column
            'ipv4_address': row[3],  # Assuming this is the IPv4 address column
            'ipv6_capable': row[4],  # Assuming this is the IPv6 capability column
            'ipv6_address': row[5]  # Assuming this is the IPv6 address column
        })
    return render_template('settings.html', dead_workers=dead_workers, active_workers=active_workers)

@app.route("/test")
def test():
    return render_template('test.html'), 200

@app.route("/output")
def output():
    return render_template('output.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8666)