import sys, os
INTERP = os.path.join(os.environ['HOME'], '.domain.com', 'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('fproject')
from fproject.app import app as application

# Uncomment next two lines to enable debugging
#from werkzeug.debug import DebuggedApplication
#application = DebuggedApplication(application, evalex=True)

#from flask import Flask
#application = Flask(__name__)

#@application.route('/')
#def index():
#	return 'Hello passenger'
