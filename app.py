from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'users'
}

# Create a database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connectiongit checkout steptech_assignment
def hello_world():
    return "Hello, World!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
        conn.commit()
        cursor.close()
        conn.close()
        return 'User added successfully!'
    return render_template('new_user.html')

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return jsonify(user)
    return 'User not found', 404

if __name__ == '__main__':
    app.run(debug=True)
