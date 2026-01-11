"""
Part 1: Hello Flask - Your First Web Server
============================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask  # Import Flask class from the flask package

app = Flask(__name__)  # Create Flask app instance, __name__ tells Flask where to look for templates/static files


@app.route('/')  # Decorator that maps URL '/' (home page) to this function
def home():
    return "<h1 style='color: blue;'>Hello Pritam! Welcome to Flask!</h1><p>This is HTML content with styling!</p><p>Learning web development is fun!</p>"


# Exercise 1.3: Add a second route
@app.route('/about')  # Maps URL '/about' to this function
def about():
    return """
    <h2>About This Website</h2>
    <p>This is my first Flask web application.</p>
    <p>I'm learning Python web development with Flask.</p>
    <ul>
        <li>Created by: <strong>Pritam</strong></li>
        <li>Date: Today</li>
        <li>Purpose: Learning Flask basics</li>
    </ul>
    <a href="/">Back to Home</a>
    """


if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload and detailed error messages