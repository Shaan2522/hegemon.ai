from flask import Flask, request, render_template, jsonify
import hegemon_chatbot as hegemon_chatbot
import os

app = Flask(__name__)

counter_file_path = 'visitor_count.txt'

def get_visitor_count():
    if not os.path.exists(counter_file_path):
        with open(counter_file_path, 'w') as file:
            file.write('0')
    with open(counter_file_path, 'r') as file:
        count = int(file.read())
    return count

def increment_visitor_count():
    count = get_visitor_count()
    count += 1
    with open(counter_file_path, 'w') as file:
        file.write(str(count))
    return count

@app.route('/')
def landing():
    visitor_count = increment_visitor_count()
    return render_template('index.html', visitor_count=visitor_count)

@app.route('/chat_page')
def chat_page():
    return render_template('chat_page.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Implement your authentication logic here
    # For now, we'll just redirect to index.html
    return redirect(url_for('chat_page'))

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    # Implement your signup logic here
    # For now, we'll just redirect to index.html
    return redirect(url_for('chat_page'))

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        user_input = request.json['message']
        response = hegemon_chatbot.generate_response(user_input)
        if response:
            return jsonify({'response': response})
        else:
            return jsonify({'response': 'Sorry, I didn\'t understand that.'}), 400
    except Exception as e:
        return jsonify({'response': 'An error occurred: {}'.format(str(e))}), 500

if __name__ == '__main__':
    app.run(debug=True)