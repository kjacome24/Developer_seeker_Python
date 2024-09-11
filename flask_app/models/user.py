from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from flask_app.models import organization
from flask_app.models import postion

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

DB = 'sightings_schema'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.country = data['country']
        self.stage_registration = data['stage_registration']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users order by first_name;"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users ( first_name , last_name , email , password, country, stage_registration, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , %(country)s , 1, NOW() , NOW() );"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        print(result)
        data_usuario = {'id': result}
        return cls.getId(data_usuario)
    
    @classmethod
    def getId(cls, data):
        query = "select * from users where id = %(id)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            print("consult was completed adn is returning none")
            return None
    @classmethod
    def getbyemail(cls, data):
        query = "select * from users where email = %(email)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
    @staticmethod
    def validate_entry(data):
        is_valid = True
        if data['which_form']=='register_user':
            if len(data['first_name']) <2:
                flash(["The first name should have at least 2 characters",0])
                is_valid= False
            if not NAME_REGEX.match(data['first_name']):
                flash(["Your first name should not have numbers",0])
                is_valid= False
            if len(data['last_name']) <2:
                flash(["The last name should have at least 2 characters",0])
                is_valid= False
            if not NAME_REGEX.match(data['last_name']):
                flash(["Your last name should not have numbers",0])
                is_valid= False
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",0])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",0])
                is_valid = False
            if data['passwordconfir'] !=data['password']:
                flash(["The password confirmation is not matching with the original password",0])
                is_valid= False
            if not PASSWORD_REGEX.match(data['password']):
                flash(["Your password should have at least 8 characters with at least one lowercase and one uppercase ASCII character and also at least one character from the set @#$%^&+=, plus a number",0])
                is_valid= False
            if data['country'] =='none':
                flash(["You should select a country",0])
                is_valid = False
        else:
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",1])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",1])
                is_valid = False
        return is_valid
    
    @staticmethod
    def validate_entry2(data):
        is_valid = True
        counter = 0
        if data['html'] !='False':
            counter +=1
        if data['css'] !='False':
            counter +=1
        if data['js'] !='False':
            counter +=1
        if data['ruby'] !='False':
            counter +=1
        if data['python'] !='False':
            counter +=1
        if data['sql'] !='False':
            counter +=1
        if data['java'] !='False':
            counter +=1
        if data['csharp'] !='False':
            counter +=1
        if data['cplus'] !='False':
            counter +=1
        if data['go'] !='False':
            counter +=1
        if data['kotlin'] !='False':
            counter +=1
        if data['php'] !='False':
            counter +=1
        if counter==0:
            flash("Please select at least one language to proceed")
            is_valid= False
        if len(data['bio']) <10:
            flash("Your bio should have at least 10 characters")
            is_valid= False
        if data['githubuser'] =='none':
            flash("You should add a valid github User to proceed")
            is_valid= False
        return is_valid
    
    @classmethod
    def save_languages(cls,data):
        query = "INSERT INTO user_languages (`html`, `css`, `js`, `ruby`, `python`, `sql`, `java`, `csharp`, `cplus`, `go`, `kotlin`, `php`, `bio`, `githubuser`, `user_id`) VALUES (%(html)s, %(css)s, %(js)s, %(ruby)s, %(python)s, %(sql)s, %(java)s, %(csharp)s, %(cplus)s, %(go)s, %(kotlin)s, %(php)s, %(bio)s, %(githubuser)s, %(user_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        query = "UPDATE users SET `stage_registration` = '2' WHERE (`id` =  %(user_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        return result
    

    @staticmethod
    def validate_entry3(data):
        is_valid = True
        counter = 0
        if data['flask'] !='False':
            counter +=1
        if data['rails'] !='False':
            counter +=1
        if data['spring'] !='False':
            counter +=1
        if data['django'] !='False':
            counter +=1
        if data['react'] !='False':
            counter +=1
        if data['bottle'] !='False':
            counter +=1
        if data['angular'] !='False':
            counter +=1
        if data['boostrap'] !='False':
            counter +=1
        if data['grails'] !='False':
            counter +=1
        if data['laravel'] !='False':
            counter +=1
        if data['blazor'] !='False':
            counter +=1
        if data['cpp'] !='False':
            counter +=1
        if counter==0:
            flash("Please select at least one framework or library!")
            is_valid= False
        return is_valid


    @classmethod
    def save_frameworks(cls,data):
        query = "INSERT INTO user_frameworks (`flask`, `rails`, `spring`, `django`, `react`, `bottle`, `angular`, `boostrap`, `grails`, `laravel`, `cpp3`, `blazor`, `user_id`) VALUES (%(flask)s, %(rails)s, %(spring)s, %(django)s, %(react)s, %(bottle)s, %(angular)s, %(boostrap)s, %(grails)s, %(laravel)s, %(cpp)s, %(blazor)s, %(user_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        query = "UPDATE users SET `stage_registration` = '3' WHERE (`id` =  %(user_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        return result


    @classmethod
    def complete_registration(cls,data):
        query = "UPDATE users SET `stage_registration` = '4' WHERE (`id` =  %(user_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        return result

class Super_user( User ):
    def __init__(self,data):
        super().__init__(data)
        self.githubuser = data['githubuser']
        self.bio = data['bio']
        self.html = data['html']
        self.css = data['css']
        self.js = data['js']
        self.ruby = data['ruby']
        self.python = data['python']
        self.sql = data['sql']
        self.java = data['java']
        self.csharp = data['csharp']
        self.cplus = data['cplus']
        self.go = data['go']
        self.kotlin = data['kotlin']
        self.php = data['php']
        self.bio = data['bio']
        self.flask = data['flask']
        self.rails = data['rails']
        self.spring = data['spring']
        self.django = data['django']
        self.react = data['react']
        self.bottle = data['bottle']
        self.angular = data['angular']
        self.boostrap = data['boostrap']
        self.grails = data['grails']
        self.laravel = data['laravel']
        self.cpp = data['cpp3']
        self.blazor = data['blazor']
        self.validator = {}
        self.match = 0
        self.match2 = 0
    @classmethod
    def get_all(cls):
        query = "select * from users as t1 left join user_languages as t2 on t1.id=t2.user_id left join user_frameworks as t3 on t1.id=t3.user_id where t1.stage_registration=4 order by t1.id desc;"
        results= connectToMySQL(DB).query_db(query)
        all_super_users = []
        for row_from_db in results:
            users_data ={
                "id": row_from_db["id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": "NA",
                "country":row_from_db["country"],
                "stage_registration": row_from_db["stage_registration"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"],
                "html" : row_from_db["html"],
                "css" : row_from_db["css"],
                "js" : row_from_db["js"],
                "ruby" : row_from_db["ruby"],
                "python" : row_from_db["python"],
                "sql" : row_from_db["sql"],
                "java" : row_from_db["java"],
                "csharp" : row_from_db["csharp"],
                "cplus" : row_from_db["cplus"],
                "go" : row_from_db["go"],
                "kotlin" : row_from_db["kotlin"],
                "php" : row_from_db["php"],
                "bio" : row_from_db["bio"],
                "githubuser" : row_from_db["githubuser"],
                "flask" : row_from_db["flask"],
                "rails" : row_from_db["rails"],
                "spring" : row_from_db["spring"],
                "django" : row_from_db["django"],
                "react" : row_from_db["react"],
                "bottle" : row_from_db["bottle"],
                "angular" : row_from_db["angular"],
                "boostrap" : row_from_db["boostrap"],
                "grails" : row_from_db["grails"],
                "laravel" : row_from_db["laravel"],
                "cpp" : row_from_db["cpp3"],
                "blazor" : row_from_db["blazor"]
                }
            super_user = (cls(row_from_db))
            all_super_users.append(super_user)
        return all_super_users

    @classmethod
    def get_filtered (cls,data):
        query = "select * from users as t1 left join user_languages as t2 on t1.id=t2.user_id left join user_frameworks as t3 on t1.id=t3.user_id where t1.stage_registration=4 and t2.html like %(html)s and t2.css like %(css)s and t2.js like %(js)s and t2.ruby like %(ruby)s and t2.python like %(python)s and t2.sql like %(sql)s and t2.java like %(java)s and t2.csharp like %(csharp)s and t2.cplus like %(cplus)s and t2.go like %(go)s and t2.kotlin like %(kotlin)s and t2.php like %(php)s and t3.flask like %(flask)s and t3.rails like %(rails)s and t3.spring like %(spring)s and t3.django like %(django)s and t3.react like %(react)s and t3.bottle like %(bottle)s and t3.angular like %(angular)s and t3.boostrap like %(boostrap)s and t3.grails like %(grails)s and t3.laravel like %(laravel)s and t3.cpp3 like %(cpp)s and t3.blazor like %(blazor)s;"
        results= connectToMySQL(DB).query_db(query, data)
        all_super_users = []
        for row_from_db in results:
            users_data ={
                "id": row_from_db["id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": "NA",
                "country":row_from_db["country"],
                "stage_registration": row_from_db["stage_registration"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"],
                "html" : row_from_db["html"],
                "css" : row_from_db["css"],
                "js" : row_from_db["js"],
                "ruby" : row_from_db["ruby"],
                "python" : row_from_db["python"],
                "sql" : row_from_db["sql"],
                "java" : row_from_db["java"],
                "csharp" : row_from_db["csharp"],
                "cplus" : row_from_db["cplus"],
                "go" : row_from_db["go"],
                "kotlin" : row_from_db["kotlin"],
                "php" : row_from_db["php"],
                "bio" : row_from_db["bio"],
                "githubuser" : row_from_db["githubuser"],
                "flask" : row_from_db["flask"],
                "rails" : row_from_db["rails"],
                "spring" : row_from_db["spring"],
                "django" : row_from_db["django"],
                "react" : row_from_db["react"],
                "bottle" : row_from_db["bottle"],
                "angular" : row_from_db["angular"],
                "boostrap" : row_from_db["boostrap"],
                "grails" : row_from_db["grails"],
                "laravel" : row_from_db["laravel"],
                "cpp" : row_from_db["cpp3"],
                "blazor" : row_from_db["blazor"]
                }
            super_user = (cls(row_from_db))
            all_super_users.append(super_user)
        return all_super_users
    
    @classmethod
    def getId(cls, data):
        query = "select * from users as t1 left join user_languages as t2 on t1.id=t2.user_id left join user_frameworks as t3 on t1.id=t3.user_id where t1.id=%(id)s;"
        results= connectToMySQL(DB).query_db(query, data)
        if len(results) > 0:
            x = cls(results[0])
            return x
        else:
            print("consult was completed adn is returning none")
            return None