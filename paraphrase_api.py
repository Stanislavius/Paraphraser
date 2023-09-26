from flask import Flask, redirect, url_for, request
from paraphraser import *
from flask import jsonify

app = Flask(__name__)

@app.route('/paraphrase', methods = ['GET'])
def paraphrase():
    args = request.args
    tree = args.get("tree", type=str)
    limit = args.get("limit", default=20, type=int)
    return jsonify(get_paraphrases(tree, limit = limit))
