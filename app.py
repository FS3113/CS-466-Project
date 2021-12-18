from flask import Flask
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.cm as cm
import numpy as np

app = Flask(__name__)

@app.route("/get", methods = ['POST', 'GET'])
def hello_world():
    return {"test": 3113}
