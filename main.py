from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True



user_signup_form = """<!doctype html>
<html>
  <body>
  <form method = "POST">
    <label for = "username">Username:
      <input id = "username" type ="text" name = "username"/>
    </label>
    <p class ="error">{username_error}</p>
        <label for = "password">Password:
      <input id = "password" type ="password" name = "password"/>
    </label>
    <p class ="error">{password_error}</p>
    <label for = "verify password">Verify Password:
      <input id = "verify_password" type="password" name = "verify_password"/>
    </label>
    <p class ="error">{verify_password_error}</p>
    <label for = "email">Email (optional):
      <input id = "email" type ="text" name="email"/>
    </label>
        <p class ="error">{email_error}</p>
        <input type= "submit" value="Submit"/>
        
    </form>
    </body>
    </html>"""

@app.route("/validate-signup")
def display_signup():
    return user_signup_form.format(username = "",username_error = "",password = "",password_error = "",verify_password = "",
    verify_password_error = "",email = "",email_error = "")

@app.route("/validate-signup", methods = ['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']


app.run()

@app.route('/')
def index():
    return form