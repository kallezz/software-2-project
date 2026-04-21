from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

# Import your route files here
# from .users import users_bp
# from .products import products_bp