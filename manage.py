from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import create_app, db
from app.models import  User,Pitch,Category,Comment

# instances for the create_app
app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db,User = User, Pitch = Pitch, Category = Category, Comment = Comment )



if __name__ == '__main__':
    manager.run()
