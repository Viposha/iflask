from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e993ef007102772e684ad667a53c839d'

from iflask import routes
