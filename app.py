from flask import Flask
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.cm as cm
import numpy as np
from flask import request
import json
import os
import subprocess

app = Flask(__name__)

@app.route("/get", methods = ['POST', 'GET'])
def hello_world():
    global s1, s2, match, mismatch, gap
    data = json.loads(request.data)
    s1 = data['seq1']
    s2 = data['seq2']
    match = data['match']
    mismatch = data['mismatch']
    gap = data['gap']

    # get_alignment()
    subprocess.run(["python3", "hirschberg.py", s1, s2, match, mismatch, gap])
    return {'msg': 'success'}
