import os
from app.factory import create_app

config = os.environ.get('FLASK_CONFIG', 'default')
app = create_app(config)
