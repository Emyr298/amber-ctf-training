from flask import Flask

from database import init_database
from services.teams import get_teams

app = Flask(__name__)
init_database()

@app.route('/', methods=['GET'])
def get_index():
    get_teams()
    return 'hmmm', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
