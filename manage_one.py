from flask_script import Manager, Server
from app import app, create_app
app = create_app


if __name__=='__main__':
    app.run()