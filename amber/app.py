from flask import Flask

from database import init_database
from ticks import setup_ticks

from routes.ctf import ctf_bp

app = Flask(__name__)
init_database()
setup_ticks()

app.register_blueprint(ctf_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
