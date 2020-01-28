from flask import Blueprint, request, jsonify
from app import db
from pony.orm import db_session
from marshmallow import ValidationError
from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5',vocab_path='textgenrnn_vocab.json',
config_path='textgenrnn_config.json')

#textgen = textgenrnn()
#textgen.train_from_file('bktestform3.csv', num_epochs=5, new_model=True)
# textgen.generate_to_file('Still.csv', n=500)


router = Blueprint('record', __name__)

@router.route('/records', methods=['GET'])
@db_session
def index():
    return textgen.generate()
