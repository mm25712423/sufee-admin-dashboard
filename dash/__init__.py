import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    # apply the blueprints to the app
    from dash import hello
    app.register_blueprint(hello.bp)
    app.add_url_rule('/', endpoint='index')

    return app