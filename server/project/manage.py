import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell

from app.database import db
from app.factory import create_app


def make_shell_context():
    return dict()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    with open('.env') as f:
        for line in f:
            var = line.strip().split('=')
            if len(var) == 2:
                os.environ[var[0]] = var[1]

config = os.getenv('FLASK_CONFIG') or 'default'

app = create_app(config)

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

# add ssl
port = os.environ.get('SERVER_PORT', 5000)
server = Server(host='0.0.0.0', port=port)
manager.add_command("runserver", server)


@manager.command
def profile(length=25, profile_dir=None):
    """Start the app under the code profile
    :param length: length restriction
    :param profile_dir: profile directory
    :return: None

    """
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


# add shell command for running tests
@manager.command
def test(coverage=False):
    """Run the unit tests.
    :param coverage: run coverage module if True
    :return: None

    """
    cov = None
    if os.getenv('FLASK_COVERAGE'):
        import coverage
        cov = coverage.coverage(branch=True, include='app/*')
        cov.start()

    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
        cov = coverage()
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if cov:
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        cov.html_report(directory=covdir)
        print('HTML version @ file://%s/index.html' % covdir)
        cov.erase()


@manager.command
def list_routes():
    from flask import url_for
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()
