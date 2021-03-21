from snakeeyes import create_app
from flask_script import Manager, Shell
from snakeeyes.blueprints.user.models import User
from snakeeyes.extensions import db

from stripe_utils import create_plan, delete_plan, list_plan

app = create_app()
manager = Manager(app)

db.app = app 

def make_shell_context():
    return dict(app=app, User=User, db=db, create_plan=create_plan, delete_plan=delete_plan, list_plan = list_plan )
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()


