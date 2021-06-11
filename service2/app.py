from flask import Flask
import random

from flask import Flask

app = Flask(__name__)

@app.route('/encounter', methods=['GET'])
def encounter():
    encounters = ["a giant rat","a giant goat","a pack of firebreathing lizards","a very small dwarf","an evil pig summoning wizard"]
    return  random.choice(encounters)

if __name__=="__main__": app.run(port=5001, host='0.0.0.0', debug=True)  