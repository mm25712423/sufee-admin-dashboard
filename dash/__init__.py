from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY='dev',
    # store the database in the instance folder
    DATABASE=os.path.join(app.instance_path, 'dash.sqlite'),
)

socketio = SocketIO(app, async_mode='gevent')
# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# register the database commands
from dash import db
db.init_app(app)

# apply the blueprints to the app
#from cloud import auth, instance
import dash.auth
app.register_blueprint(dash.auth.bp)
import dash.server
app.register_blueprint(dash.server.bp)

app.add_url_rule('/', endpoint='index')

app.config['SECRET_KEY'] = 'secret!'

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
