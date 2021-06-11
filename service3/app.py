from flask import Flask
import random

from flask import Flask

app = Flask(__name__)

@app.route('/location', methods=['GET'])
def location():
    locations = ["in a forested valley","on top of a mountain","in a cave","on the outskirts of a city","while walking into a swamp"]
    return  random.choice(locations)

if __name__=="__main__": app.run(port=5002, host='0.0.0.0', debug=True)  