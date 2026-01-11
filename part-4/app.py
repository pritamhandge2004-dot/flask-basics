"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""

from flask import Flask, render_template, url_for, request, redirect
import uuid  # For Exercise 4.1 - UUID demo

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', student_name="Pritam")


@app.route('/user/<username>')  # <username> captures any text from URL, visit: /user/Alice, /user/Bob
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')  # <int:post_id> captures only integers, /post/abc returns 404
def show_post(post_id):
    posts = {  # Simulated post data (in real apps, this comes from a database)
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...', 'author': 'Pritam'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...', 'author': 'Pritam'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...', 'author': 'Pritam'},
    }
    post = posts.get(post_id)  # Get the post or None if not found
    return render_template('post.html', post_id=post_id, post=post)


@app.route('/user/<username>/post/<int:post_id>')  # Multiple dynamic segments, visit: /user/Alice/post/1
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')  # Trailing slash means both /about and /about/ work
def about():
    return render_template('about.html')


@app.route('/links')  # Demonstrates url_for() - generates URLs dynamically (better than hardcoding!)
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)


# =============================================================================
# EXERCISE SOLUTIONS
# =============================================================================

# Exercise 4.1: Create a product page
@app.route('/product/<int:product_id>')
def product_page(product_id):
    # Simulated product database
    products = {
        101: {'name': 'Laptop', 'price': 899.99, 'category': 'Electronics', 'description': 'High-performance laptop'},
        102: {'name': 'Smartphone', 'price': 699.99, 'category': 'Electronics', 'description': 'Latest smartphone model'},
        103: {'name': 'Headphones', 'price': 149.99, 'category': 'Electronics', 'description': 'Noise-cancelling headphones'},
        201: {'name': 'T-Shirt', 'price': 19.99, 'category': 'Clothing', 'description': 'Cotton t-shirt'},
        202: {'name': 'Jeans', 'price': 49.99, 'category': 'Clothing', 'description': 'Denim jeans'},
    }
    
    product = products.get(product_id)
    return render_template('product.html', product_id=product_id, product=product)


# Exercise 4.2: Category and product route
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    # Simulated database with category filtering
    products = {
        'electronics': {
            101: {'name': 'Laptop', 'price': 899.99},
            102: {'name': 'Smartphone', 'price': 699.99},
            103: {'name': 'Headphones', 'price': 149.99},
        },
        'clothing': {
            201: {'name': 'T-Shirt', 'price': 19.99},
            202: {'name': 'Jeans', 'price': 49.99},
            203: {'name': 'Jacket', 'price': 89.99},
        },
        'books': {
            301: {'name': 'Python Programming', 'price': 39.99},
            302: {'name': 'Web Development', 'price': 29.99},
        }
    }
    
    category_products = products.get(category_name.lower(), {})
    product = category_products.get(product_id)
    
    return render_template('category_product.html', 
                          category_name=category_name, 
                          product_id=product_id, 
                          product=product,
                          category_products=category_products)


# Exercise 4.3: Search route
@app.route('/search/<query>')
def search_results(query):
    # Simulated search results
    all_items = [
        {'name': 'Python Flask Tutorial', 'type': 'Book', 'price': 29.99},
        {'name': 'Web Development Course', 'type': 'Course', 'price': 99.99},
        {'name': 'Programming Laptop', 'type': 'Electronics', 'price': 899.99},
        {'name': 'Code Editor', 'type': 'Software', 'price': 0.00},
        {'name': 'Flask Web Framework', 'type': 'Library', 'price': 0.00},
        {'name': 'Python Programming', 'type': 'Book', 'price': 39.99},
    ]
    
    # Simple search logic (case-insensitive)
    results = [item for item in all_items if query.lower() in item['name'].lower()]
    
    return render_template('search.html', query=query, results=results, total_results=len(results))


# Bonus for Exercise 4.3: Search form that redirects
@app.route('/search-form', methods=['GET', 'POST'])
def search_form():
    if request.method == 'POST':
        query = request.form.get('search_query', '').strip()
        if query:
            return redirect(url_for('search_results', query=query))
    
    return render_template('search_form.html')


# Bonus: Additional routes to demonstrate other parameter types
@app.route('/price/<float:amount>')
def show_price(amount):
    return render_template('price.html', amount=amount)


@app.route('/file/<path:filepath>')
def show_file(filepath):
    return render_template('file.html', filepath=filepath)


@app.route('/uuid/<uuid:uuid_value>')
def show_uuid(uuid_value):
    return render_template('uuid.html', uuid_value=uuid_value)


if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Changed port to avoid conflicts