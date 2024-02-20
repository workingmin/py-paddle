import os

bind = '0.0.0.0:5555'
daemon = True
timeout = 300

workers = 4
threads = 2

root = os.path.dirname(os.path.abspath(__file__))
accesslog = os.path.join(root, 'gunicorn.access.log')
errorlog = os.path.join(root, 'gunicorn.error.log')
loglevel = "debug"