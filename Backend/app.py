from flask import Flask, render_template, request, redirect, url_for, flash
import os

# Absolute paths for templates and static folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # backend folder path
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'Frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'Frontend', 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = "mysecretkey"

# Dummy user credentials
USER_CREDENTIALS = {
    "pragnesh": "12345"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return render_template('dashboard.html', username=username)
        else:
            flash("Invalid username or password!", "error")
            return redirect(url_for('login'))
    return render_template('login.html')

if __name__ == '__main__':
    # Debug prints to verify paths
    print("Templates folder:", TEMPLATE_DIR)
    print("Static folder:", STATIC_DIR)
    app.run(debug=True)
