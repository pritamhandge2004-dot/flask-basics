"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Change from "Alex" to "Pritam"
    student_name = "Pritam"
    return render_template('index.html', name=student_name)  # Pass variable to template as {{ name }}


@app.route('/profile')
def profile():
    # Exercise 3.1: Add more fields to the profile
    user_data = {
        'name': 'Pritam',
        'age': 25,  # Changed age
        'course': 'Web Development with Flask',
        'is_enrolled': True,
        # New fields added for Exercise 3.1
        'email': 'pritam@example.com',
        'city': 'Kolkata',
        'phone': '+91 98765 43210',
        'enrollment_date': '2024-01-15',
        'current_semester': 3,
        'cgpa': 8.7
    }
    return render_template('profile.html', 
                           # Passing individual variables
                           name=user_data['name'],
                           age=user_data['age'],
                           course=user_data['course'],
                           is_enrolled=user_data['is_enrolled'],
                           # New variables for Exercise 3.1
                           email=user_data['email'],
                           city=user_data['city'],
                           phone=user_data['phone'],
                           enrollment_date=user_data['enrollment_date'],
                           semester=user_data['current_semester'],
                           cgpa=user_data['cgpa'])


@app.route('/skills')
def skills():
    # Updated skills list with more items
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask', 'SQL', 'Git', 'Bootstrap', 'Jinja2']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template


@app.route('/projects')
def projects():
    project_list = [  # List of dictionaries - common pattern for database-like data
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS', 'description': 'My portfolio website'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask', 'description': 'Blog application with user auth'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript', 'description': 'Real-time weather dashboard'},
        {'name': 'E-commerce API', 'status': 'Completed', 'tech': 'Python/Flask/MySQL', 'description': 'REST API for online store'},
        {'name': 'Task Manager', 'status': 'In Progress', 'tech': 'Python/Tkinter', 'description': 'Desktop task management app'},
    ]
    return render_template('projects.html', projects=project_list)


# Exercise 3.3: Create a grades page
@app.route('/grades')
def grades():
    # Dictionary of subjects and grades
    grades_data = {
        'Python Programming': 'A+',
        'Web Development': 'A',
        'Database Systems': 'B+',
        'Data Structures': 'A',
        'Operating Systems': 'A-',
        'Computer Networks': 'B+',
        'Software Engineering': 'A',
        'Mathematics': 'A-',
        'English': 'A',
        'Project Work': 'A+'
    }
    
    # Calculate statistics
    grade_points = {
        'A+': 10, 'A': 9, 'A-': 8, 'B+': 7, 'B': 6, 'B-': 5,
        'C+': 4, 'C': 3, 'C-': 2, 'D': 1, 'F': 0
    }
    
    total_points = sum(grade_points.get(grade, 0) for grade in grades_data.values())
    average_grade = total_points / len(grades_data)
    
    # Count grades
    grade_counts = {}
    for grade in grades_data.values():
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    return render_template('grades.html',
                           grades=grades_data,
                           average_grade=round(average_grade, 2),
                           grade_counts=grade_counts,
                           student_name="Pritam")


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Changed port to avoid conflicts