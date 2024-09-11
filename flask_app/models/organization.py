from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from flask_app.models import user
from flask_app.models import postion

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

DB = 'sightings_schema'

class Organization:
    def __init__( self , data ):
        self.id = data['id']
        self.org_name = data['org_name']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.address = data['address']
        self.country = data['country']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orgs order by org_name;"
        results = connectToMySQL(DB).query_db(query)
        orgs = []
        for org in results:
            orgs.append( cls(org) )
        return orgs
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO orgs (org_name, first_name, last_name, email, address, country, password, created_at, updated_at) VALUES (%(org_name)s, %(first_name)s,  %(last_name)s, %(email)s, %(address)s, %(country)s , %(password)s, NOW() , NOW() );"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        data_usuario = {'id': result}
        return cls.getId(data_usuario)
    
    @classmethod
    def getId(cls, data):
        query = "select * from orgs where id = %(id)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            print("consult was completed adn is returning none")
            return None

    @classmethod
    def getbyemail(cls, data):
        query = "select * from orgs where email = %(email)s;"
        mysql = connectToMySQL(DB)
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if data['which_form']=='register_organization':
            if len(data['org_name']) <3:
                flash(["The name of your organization should have at least 3 characters",4])
                is_valid= False
            if len(data['first_name']) <2:
                flash(["The first name should have at least 2 characters",4])
                is_valid= False
            if not NAME_REGEX.match(data['first_name']):
                flash(["Your first name should not have numbers",4])
                is_valid= False
            if len(data['last_name']) <2:
                flash(["The last name should have at least 2 characters",4])
                is_valid= False
            if not NAME_REGEX.match(data['last_name']):
                flash(["Your last name should not have numbers",4])
                is_valid= False
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",4])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",4])
                is_valid = False
            if data['passwordconfir'] !=data['password']:
                flash(["The password confirmation is not matching with the original password",4])
                is_valid= False
            if not PASSWORD_REGEX.match(data['password']):
                flash(["Your password should have at least 8 characters with at least one lowercase and one uppercase ASCII character and also at least one character from the set @#$%^&+=, plus a number",4])
                is_valid= False
            if data['country'] =='none':
                flash(["You should select a country",4])
                is_valid = False
            if len(data['address']) <5:
                flash(["The address should have at least 5 characters",4])
                is_valid = False
        else:
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",3])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",3])
                is_valid = False
        return is_valid
