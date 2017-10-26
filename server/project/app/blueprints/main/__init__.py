from flask import Blueprint

url_prefix = '/'
main = Blueprint('main', __name__, url_prefix=url_prefix,
                template_folder='templates')

from .views import *