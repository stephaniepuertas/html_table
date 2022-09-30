from flask import Flask, render_template
from all_users import users

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users= users)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)