"""
Part 5: Mini Project - Personal Website with Flask
===================================================
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA
# =============================================================================

PERSONAL_INFO = {
    'name': 'Pritam Handge',
    'title': 'Web Developer',
    'bio': 'Python developer passionate about building web applications with Flask.',
    'email': 'pritamhandge2004@gmail.com',
    'github': 'https://github.com/pritamhandge2004-dot',
    'linkedin': 'https://www.linkedin.com/in/pritam-handge-a3909a33a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app',
}

SKILLS = [
    {'name': 'Python', 'level': 85},
    {'name': 'HTML/CSS', 'level': 80},
    {'name': 'Flask', 'level': 75},
    {'name': 'JavaScript', 'level': 65},
    {'name': 'SQL', 'level': 70},
]

PROJECTS = [
    {'id': 1, 'name': 'Portfolio Website', 'description': 'My personal portfolio website built with Flask.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Task Manager', 'description': 'A simple task management app.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather App', 'description': 'Weather application using API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]

BLOG_POSTS = [
    {'id': 1, 'title': 'Flask Introduction', 'date': '2024-01-10', 'content': 'Learn Flask basics...', 'category': 'Tutorial'},
    {'id': 2, 'title': 'Jinja2 Templates', 'date': '2024-01-15', 'content': 'Master Jinja2 templating...', 'category': 'Tutorial'},
]

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', 
                         info=PERSONAL_INFO, 
                         projects=PROJECTS,
                         skills=SKILLS)

@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)

@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', 
                         info=PERSONAL_INFO, 
                         project=project, 
                         project_id=project_id,
                         projects=PROJECTS)

@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)

@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    filtered_projects = []
    for project in PROJECTS:
        if skill_name.lower() in [tech.lower() for tech in project['tech']]:
            filtered_projects.append(project)
    
    return render_template('skill_projects.html', 
                         info=PERSONAL_INFO, 
                         skill_name=skill_name, 
                         projects=filtered_projects)

if __name__ == '__main__':
    app.run(debug=True, port=5000)