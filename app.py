from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/api/data')
def get_data():
    return jsonify({'message': 'API response', 'status': 'success'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({'received': data, 'status': 'created'})

@app.route('/form')
def form():
    return render_template_string('''
    <form method="POST" action="/submit">
        <input type="text" name="name" placeholder="Your name" required>
        <button type="submit">Submit</button>
    </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Form submitted! Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)