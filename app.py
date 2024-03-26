#Flask information could be found here: https://pythonbasics.org/what-is-flask-python/
from flask import Flask
from route import *

#initialize a flask object
app = Flask(__name__)

#from webpage https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe
app.config.update(dict(
    SECRET_KEY="nyawuwunyanya",
    WTF_CSRF_SECRET_KEY="csrf fffffwwwww"
))

#something that is like a main() in java
if __name__ == "__main__":
    app.run(debug = True)
