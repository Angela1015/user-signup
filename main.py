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
    
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if username =="":
        username_error = "Please enter a name"
        username = ""
    else:
        if len(username)>20 or len(username)<3:
            username_error = "Username must be between 3 and 20 characters"
            username = ""

    if password =="":
        password_error = "Please enter a password"
        password_error = ""
    else:
        if len(password)>20 or len(password)<3:
            password_error = "Password must be between 3 and 20 characters"
            password = ""       



    if not username_error and not password_error:
        return "success" 

    else:
        return user_signup_form.format(username=username,username_error=username_error,password=password,password_error=password_error,
      verify_password=verify_password,verify_password_error=verify_password_error,email=email,email_error=email_error)    
    
app.run()

@app.route('/')
def index():
    return form