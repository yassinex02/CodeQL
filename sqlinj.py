from flask import Flask, request
import sqlite3

app = Flask(__name__)


def fetch_user(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = ?;"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user


@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    if user_id is None:
        return "Please provide a user ID.", 400

    user = fetch_user(user_id)
    if user:
        return f"User Found: {user}", 200
    else:
        return "No user found.", 404


if __name__ == "__main__":
    app.run(debug=False)
