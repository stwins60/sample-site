from flask import Flask, render_template, request, redirect, url_for



my_personal_page = Flask(__name__)

FLASK_ENV = 'development'
FLASK_DEBUG = True



@my_personal_page.route('/')
def home():
    return render_template('index.html')

@my_personal_page.route('/about')
def about():
    return render_template('about.html')

@my_personal_page.route('/contact')
def contact():
    return render_template('contact.html')

@my_personal_page.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')


if __name__ == '__main__':
    my_personal_page.run(debug=True, host='0.0.0.0', port=5000)
