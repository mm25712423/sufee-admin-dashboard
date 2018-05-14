from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from dash.auth import login_required
from dash.db import get_db
from flask import current_app

bp = Blueprint('server', __name__)


@bp.route('/')
@login_required
def index():
    current_app.logger.info("Index")
    return render_template('index.html')
