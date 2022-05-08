class User:
    '''
    User class to define user object
    '''

    def __init__(self,id, name,email,password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


class Comment:
    '''
    Comment class to define comment object
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description
