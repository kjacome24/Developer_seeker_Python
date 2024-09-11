from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_bcrypt import Bcrypt

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST': ##########We make sure we are entering by a post request.
        if not User.validate_entry(request.form): ###### We validate the entry in both forms
            return redirect('/')
        if request.form.get("which_form")=='register_user': ######If is the first form of regestiring. 
            data = {
            "first_name" : request.form.get("first_name"),
            "last_name" : request.form.get("last_name"),
            "email" : request.form.get("email"),
            "password" : bcrypt.generate_password_hash(request.form.get("password")),
            "country" : request.form.get("country")
            }
            user=User.getbyemail(data)
            if user is not None:
                flash(["Email address has been already registered!",0])
                return redirect('/')
            user=User.save(data)
            session["id"] = user.id
            session["first_name"] = user.first_name
            session["last_name"] = user.last_name
            session["email"] = user.email
            data = {'sender_id': session['id']}
            return redirect('/dashboard')
        elif request.form.get("which_form")=='log_in':
            data = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
            }
            user=User.getbyemail(data)
            if user is None or  not bcrypt.check_password_hash(user.password, data['password']):
                flash(["Invalid Email/Password",1])
                return redirect('/')
            session["id"] = user.id
            session["first_name"] = user.first_name
            session["last_name"] = user.last_name
            session["email"] = user.email
            return redirect('/dashboard')
    else:
        return render_template("index_devs_on_deck.html")

@app.route('/index')
def index_devs_on_deck():
    return render_template("index_devs_on_deck.html")


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {'id':session['id']}
        user = User.getId(data)
        print(user.stage_registration)
        if user.stage_registration == 1:
            return render_template("xxx.html")
        elif user.stage_registration == 2:
            return render_template("xxx2.html")
        elif user.stage_registration == 3:
            return render_template("xxx3.html")
        else:
            return render_template("dashboard.html", user=user)


@app.route('/destroy',methods=['GET', 'POST'])
def log_out():
    session.clear()
    return redirect ('/')

@app.route('/second_step_registration', methods=["POST"])
def second_step_registration():
    if session.get('id') == None:
        return redirect('/')
    else:
        if not User.validate_entry2(request.form):
            return redirect('/dashboard')
        data = {
                "html" : request.form.get("html"),
                "css" : request.form.get("css"),
                "js" : request.form.get("js"),
                "ruby" : request.form.get("ruby"),
                "python" : request.form.get("python"),
                "sql" : request.form.get("sql"),
                "java" : request.form.get("java"),
                "csharp" : request.form.get("csharp"),
                "cplus" : request.form.get("cplus"),
                "go" : request.form.get("go"),
                "kotlin" : request.form.get("kotlin"),
                "php" : request.form.get("php"),
                "bio" : request.form.get("bio"),
                "githubuser" : request.form.get("githubuser"),
                "user_id": session['id']}
        User.save_languages(data)
    return redirect('/dashboard')


@app.route('/third_step_registration', methods=["POST"])
def third_step_registration():
    if session.get('id') == None:
        return redirect('/')
    else:
        if not User.validate_entry3(request.form):
            return redirect('/dashboard')
        data = {
                "flask" : request.form.get("flask"),
                "rails" : request.form.get("rails"),
                "spring" : request.form.get("spring"),
                "django" : request.form.get("django"),
                "react" : request.form.get("react"),
                "bottle" : request.form.get("bottle"),
                "angular" : request.form.get("angular"),
                "boostrap" : request.form.get("boostrap"),
                "grails" : request.form.get("grails"),
                "laravel" : request.form.get("laravel"),
                "cpp" : request.form.get("cpp"),
                "blazor" : request.form.get("blazor"),
                "user_id": session['id']}
        User.save_frameworks(data)
    return redirect('/dashboard')


@app.route('/last_step_registration', methods=["POST"])
def last_step_registration():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {
                "user_id": session['id']}
        User.complete_registration(data)
    return redirect('/dashboard')




