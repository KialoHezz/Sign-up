# imported db instance
from app import create_app,db
from app.models import User

# create a instance 
app = create_app('development')


if __name__ == '__main__':
    app.run()
