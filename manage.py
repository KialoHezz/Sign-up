# imported db instance
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
from app.models import Role, User

# create a instance 
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

# create shell contextlib
# run flask shell
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role)




if __name__ == '__main__':
    manager.run()
