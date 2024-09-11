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

@app.route('/position/<int:id>', methods=['GET', 'POST'])
def position_by_id(id):
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {'id':session['id']}

        org = Organization.getId(data)
        super_users = Super_user.get_all()
        data = {"id" : id}
        position = Position.get_one(data)
        print(vars(position))
        for key, value in vars(position).items():
            if value=="True":
                position.validator += 1
                position.validator2[key]= value
        print(position.validator2)
        for user in super_users:
            x = vars(user).items()
            for key, value in x:
                if value=="True":
                    user.validator[key]= value
            print(f"Here the trues {user.validator}")
            z = user.validator.keys() & position.validator2.keys()
            print(f"Here the match{z}" )
            if len(z)==0:
                w = 0
            else:
                w = (len(z)/position.validator)*100
            rounded_num = round(w)
            user.match = rounded_num
            user.match2 = user.match
            user.match=(f"{rounded_num}%")
        print(super_users)
        Position.selectionSort(super_users)
        super_users.reverse()
        return render_template("position.html", org=org, super_users=super_users,position=position)

@app.route('/position/new', methods=['GET', 'POST'])
def list_new_postion():
    if session.get('id') == None:
        return redirect('/')
    else:
        return render_template("xxx4.html")
    

@app.route('/creating_new', methods=["POST"])
def creating_new():
    if session.get('id') == None:
        return redirect('/')
    else:
        data = {
                "position_name": request.form.get("position_name"),
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
                "org_id" : session['id']
                }
        if not Position.validate_entry(data):
            return redirect('/position/new')
        Position.save_position(data)
        return redirect('/org/dashboard')
    

