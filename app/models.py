from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

# Authentication of user object
'''
pass db.Model as arqument to connect our class User and allow communication btn class and db
'''
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password_secure = db.Column(db.String(50))


    @property
    def password(self):
        raise AttributeError('Cannot read paasword attribute')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        '''
        __repr___ make easy to debug our application
        '''
        return f'User {self.name} {self.email} {self.password}'


class Comment:
    '''
    Comment class to define comment object
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

# decorate that is acallback function to handle User
@login_manager.user_loader
# function that queries a database and get the user with id
def load_user(user_id):
    return User.query.get(int(user_id))


