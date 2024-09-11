from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.user import Super_user 
from flask_app.models.organization import Organization
from flask_app.models.postion import Position
from flask_bcrypt import Bcrypt

# Creación de objeto Bcrypt
bcrypt = Bcrypt(app)

###############ORG

@app.route('/org', methods=['GET', 'POST'])
def index2():
    if request.method =='POST': ##########We make sure we are entering by a post request.
        if not Organization.validate_entry(request.form): ###### We validate the entry in both forms
            return redirect('/')
        if request.form.get("which_form")=='register_organization': ######If is the first form of regestiring. 
            data = {
            "org_name" : request.form.get("org_name"),
            "first_name" : request.form.get("first_name"),
            "last_name" : request.form.get("last_name"),
            "email" : request.form.get("email"),
            "address" : request.form.get("address"),
            "password" : bcrypt.generate_password_hash(request.form.get("password")),
            "country" : request.form.get("country")
            }
            org=Organization.getbyemail(data)
            if org is not None:
                flash(["Email address has been already registered!",4])
                return redirect('/')
            org=Organization.save(data)
            session["id"] = org.id
            session["org_name"] = org.org_name
            session["first_name"] = org.first_name
            session["last_name"] = org.last_name
            session["email"] = org.email
            return redirect('/org/dashboard')
        elif request.form.get("which_form")=='log_in_organization':
            data = {
            "email" : request.form.get("email"),
            "password" : request.form.get("password")
            }
            org=Organization.getbyemail(data)
            if org is None or  not bcrypt.check_password_hash(org.password, data['password']):
                flash(["Invalid Email/Password",3])
                return redirect('/')
            session["id"] = org.id
            session["org_name"] = org.org_name
            session["first_name"] = org.first_name
            session["last_name"] = org.last_name
            session["email"] = org.email
            return redirect('/org/dashboard')
    else:
        return render_template("index_devs_on_deck.html")



@app.route('/org/dashboard', methods=['GET', 'POST'])
def org_dashboard():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {'id':session['id']}
        org = Organization.getId(data)
        super_users = Super_user.get_all()
        positions = Position.get_all()
        print(positions)
        return render_template("dashboard_org.html", org=org, super_users=super_users,positions=positions)
    

@app.route('/filtering', methods=["POST"])
def filtering():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {}
        counter = 0
        if request.form.get("html") is None:
            data["html"] = "%%"
        else:
            data["html"] = "True"
            counter += 1
        if request.form.get("css") is None:
            data["css"] = "%%"
        else:
            data["css"] = "True"
            counter += 1
        if request.form.get("js") is None:
            data["js"] = "%%"
        else:
            data["js"] = "True"
            counter += 1
        if request.form.get("ruby") is None:
            data["ruby"] = "%%"
        else:
            data["ruby"] = "True"
            counter += 1
        if request.form.get("python") is None:
            data["python"] = "%%"
        else:
            data["python"] = "True"
            counter += 1
        if request.form.get("sql") is None:
            data["sql"] = "%%"
        else:
            data["sql"] = "True"
            counter += 1
        if request.form.get("java") is None:
            data["java"] = "%%"
        else:
            data["java"] = "True"
            counter += 1
        if request.form.get("csharp") is None:
            data["csharp"] = "%%"
        else:
            data["csharp"] = "True"
            counter += 1
        if request.form.get("cplus") is None:
            data["cplus"] = "%%"
        else:
            data["cplus"] = "True"
            counter += 1
        if request.form.get("go") is None:
            data["go"] = "%%"
        else:
            data["go"] = "True"
            counter += 1
        if request.form.get("kotlin") is None:
            data["kotlin"] = "%%"
        else:
            data["kotlin"] = "True"
            counter += 1
        if request.form.get("php") is None:
            data["php"] = "%%"
        else:
            data["php"] = "True"
            counter += 1
        if request.form.get("flask") is None:
            data["flask"] = "%%"
        else:
            data["flask"] = "True"
            counter += 1
        if request.form.get("rails") is None:
            data["rails"] = "%%"
        else:
            data["rails"] = "True"
            counter += 1
        if request.form.get("spring") is None:
            data["spring"] = "%%"
        else:
            data["spring"] = "True"
            counter += 1
        if request.form.get("django") is None:
            data["django"] = "%%"
        else:
            data["django"] = "True"
            counter += 1
        if request.form.get("react") is None:
            data["react"] = "%%"
        else:
            data["react"] = "True"
            counter += 1
        if request.form.get("bottle") is None:
            data["bottle"] = "%%"
        else:
            data["bottle"] = "True"
            counter += 1
        if request.form.get("angular") is None:
            data["angular"] = "%%"
        else:
            data["angular"] = "True"
            counter += 1
        if request.form.get("boostrap") is None:
            data["boostrap"] = "%%"
        else:
            data["boostrap"] = "True"
            counter += 1
        if request.form.get("grails") is None:
            data["grails"] = "%%"
        else:
            data["grails"] = "True"
            counter += 1
        if request.form.get("laravel") is None:
            data["laravel"] = "%%"
        else:
            data["laravel"] = "True"
            counter += 1
        if request.form.get("cpp") is None:
            data["cpp"] = "%%"
        else:
            data["cpp"] = "True"
            counter += 1
        if request.form.get("blazor") is None:
            data["blazor"] = "%%"
        else:
            data["blazor"] = "True"
            counter += 1
        if counter == 0:
            return redirect('/org/dashboard')
        else:
            data2 = {'id':session['id']}
            org = Organization.getId(data2)
            super_users = Super_user.get_filtered(data)
            positions = Position.get_all()
            return render_template("dashboard_org.html", org=org, super_users=super_users,positions=positions)
        

@app.route('/org/user/<int:id>', methods=['GET', 'POST'])
def orguser_view(id):
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {"id" : id}
        user = Super_user.getId(data)
        return render_template("user_profile.html", user=user)