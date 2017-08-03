#  # An instance of the Flask class will be our WSGI application.
# from flask import Flask
# # We create an instance of the Flask class
# # Since we are creating a single module, we use __name__
# 	# this is the name of the application's module or package
# app = Flask(__name__)

# # Tells Flask what URL should trigger our function
# # @app.route('/')
# # def index():
# #     return 'index page'

# @app.route('/hello')
# # Function is given a name which is also used to generate URLs for this function
# def hello_world():
#     return 'hello'

# # Variable name is between <>
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# # <int: is a converter
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


# # TODO: Decide if we should omit trailing / by default
# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'




# # from flask import Flask, url_for
# # app = Flask(__name__)
# # @app.route('/')
# #    def index(): pass
  
# # @app.route('/login')
# #    def login(): pass
  
# # @app.route('/user/<username>')
# #    def profile(username): pass
  
# # with app.test_request_context():
# #     print url_for('index')
# #     print url_for('login')
# #     print url_for('login', next='/')
# #     print url_for('profile', username='John Doe')

# from flask import abort, redirect, url_for

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)