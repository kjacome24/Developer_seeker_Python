from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from flask_app.models import organization
from flask_app.models import user

DB = 'sightings_schema'

class Position:
    def __init__( self , data ):
        self.id = data['id']
        self.position_name = data['position_name']
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
        self.org = ''
        self.validator = 0
        self.validator2 = {}

    @classmethod
    def get_all(cls):
        query = "select * from positions;"
        results= connectToMySQL(DB).query_db(query)
        all_positions = []
        for row_from_db in results:
            org_data = {"id" : row_from_db["org_id"]}
            org = organization.Organization.getId(org_data)
            position = (cls(row_from_db))
            position.org = org
            all_positions.append(position)
        return all_positions

    @classmethod
    def get_one(cls,data):
        query = "select * from positions where id=%(id)s;"
        row_from_db = connectToMySQL(DB).query_db(query,data)
        position = cls(row_from_db[0])
        org_data = {'id' : row_from_db[0]["org_id"]}
        org = organization.Organization.getId(org_data)
        position.org = org
        return position

    @classmethod
    def save_position(cls,data):
        query = "INSERT INTO positions (`position_name`,`html`, `css`, `js`, `ruby`, `python`, `sql`, `java`, `csharp`, `cplus`, `go`, `kotlin`, `php`,`flask`, `rails`, `spring`, `django`, `react`, `bottle`, `angular`, `boostrap`, `grails`, `laravel`, `cpp3`, `blazor`,`org_id`) VALUES (%(position_name)s,%(html)s, %(css)s, %(js)s, %(ruby)s, %(python)s, %(sql)s, %(java)s, %(csharp)s, %(cplus)s, %(go)s, %(kotlin)s, %(php)s, %(flask)s, %(rails)s, %(spring)s, %(django)s, %(react)s, %(bottle)s, %(angular)s, %(boostrap)s, %(grails)s, %(laravel)s, %(cpp)s, %(blazor)s, %(org_id)s);"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        return result

    @staticmethod
    def validate_entry(data):
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
            flash("Please select at least one language to proceed")
        if len(data['position_name']) <5:
            flash("The position's name should have at least 5 characters")
            is_valid= False
        return is_valid

    @staticmethod
    def selectionSort(array):
        size = len(array)-1
        for ind in range(0,size): 
            print(f"Original loop {ind}--------------------------")
            min_index = ind
            for j in array[min_index+1:0:-1]: 
                print(f"This is the pointer{array[min_index+1].match2}")
                if array[min_index+1].match2 < j.match2:
                    print("True")
                    x= array.pop(min_index+1)
                    array.insert(min_index,x)
                    min_index = min_index -1
                else:
                    print("False")
                print(array)