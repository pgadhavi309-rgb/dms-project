from flask import Flask, render_template
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend/templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('login.html')  # yahan exactly wahi file name likho jo templates me hai

if __name__ == "__main__":
    app.run(debug=True)
