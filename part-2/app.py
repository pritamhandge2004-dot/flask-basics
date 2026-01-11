"""
Part 2: Templates - Rendering HTML Files
=========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template  # render_template lets us serve HTML files

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # Flask looks in 'templates/' folder for this file


@app.route('/about')
def about():
    return render_template('about.html')  # Renders templates/about.html


# Exercise 2.2: Create a new page - Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Renders templates/contact.html


if __name__ == '__main__':
    app.run(debug=True)