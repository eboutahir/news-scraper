import os
from flask import Flask, render_template, json
from configs import dbconfig
from bson.json_util import dumps

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@app.route("/")
def get_data():
    columns = json.load(open(os.path.join(SITE_ROOT, "static/data", "columns.json")))
    col_results = dumps(dbconfig.col.find({}, {'_id': False}).limit(30))
    return render_template('simple.html', tables=col_results, columns=columns)
