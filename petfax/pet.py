from flask import ( Blueprint, render_template )

import json

pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/<index>')
def showcase(index):
    index = int(index)
    index = index - 1
    # print(pets[index])
    # return render_template('showcase.html', pets=pets, index=index)
    return render_template('showcase.html', pet=pets[index])

@bp.route('/newfact')
def newfact():
    return render_template('newfact.html')

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)
