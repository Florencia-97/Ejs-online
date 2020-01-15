from flask import Blueprint, render_template

tutorial_blueprint = Blueprint('tutorial', __name__)

# SOBRE LA PÁGINA
@tutorial_blueprint.route('/tutorial')
def tutorial():
    return render_template("tutorial.html")