from flask import Flask, request, render_template, jsonify
import hegemon_chatbot as hegemon_chatbot

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

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