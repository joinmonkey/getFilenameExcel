# from curses.ascii import US
from flask import Flask

app = Flask(__name__)

@app.route("/abc")
def hello_world():
    return "<p>Hello, World!</p>"

# from flask import url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# url_for('static', filename='style.css')

class User:

   def __init__(self, name, theme):
      self.name = name
      self.theme = theme
   
user1 = User(name='hjm',theme='dark')
user2 = User(name='tzh',theme='dark')

# @app.route("/me")
# def me_api():
#     # user = get_current_user
#     return {
#         "username": user1.name,
#         "theme": user1.theme,
#         # "image": url_for("user_image", filename=user.image),
#     }

# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

