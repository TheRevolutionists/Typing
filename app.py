from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Routes for each page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., save to a database, send an email)
        print(f"Received message from {name} ({email}): {message}")
        return jsonify({"status": "success", "message": "Thank you for contacting us!"})
    return render_template('contact.html')

# Static files setup
@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

if __name__ == '__main__':
    app.run(debug=True)
