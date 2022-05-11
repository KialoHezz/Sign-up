from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager

# Authentication of user object
'''
pass db.Model as arqument to connect our class User and allow communication btn class and db
'''
# decorate that is acallback function to handle User
# function that queries a database and get the user with id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200))
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    password_secure = db.Column(db.String(300))
    
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    

    def __repr__(self):
        return f'User {self.username} {self.email} {self.password_secure}'


    @property
    def password(self):
        raise AttributeError('Cannot read paasword attribute')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure, password)

   

class Comment:
    '''
    Comment class to define comment object
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description


class Role(db.Model,UserMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)

    # lazy dynamic 
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        '''
        __repr___ make easy to debug our application
        '''
        return f'Role {self.title}'

