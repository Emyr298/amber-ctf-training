from flask import Flask

from database import init_database
from ticks import setup_ticks

app = Flask(__name__)
init_database()
setup_ticks()

@app.route('/', methods=['GET'])
def get_index():
    return 'hmmm', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
