from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    curr_time = datetime.datetime.now()
    return 'Hello, world! <br>{}'.format(curr_time)
