from flask import Flask
from utils import get_all, load_candidates, get_by_pk, get_by_skill

name_file = 'candidates.json'
data = get_all(load_candidates(name_file))

app = Flask(__name__)


@app.route('/')
def index():
    str = '<pre>'
    for i in data:
        str += f'{i} \n \n'
    str += '</pre>'


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        str = f'<img src="{user.picture}">'
        str += f"<pre> {user} </pre>"
    else:
        str = 'NOT FOUND'
    return str


@app.route('/skills/<x>')
def get_users(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        str = '<pre>'
        for i in data:
            str += f'{i} \n \n'
        str += '</pre>'
    else:
        str = 'NOT FOUND'
    return str


if __name__ == '__main__':

    app.run(port=1111)
