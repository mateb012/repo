
from flask import Flask
app = Flask(__name__)   # Flask constructor 

# A decorator used to tell the application 
# which URL is associated function


@app.route('/')
def hello():
    return """<message>
   <b>Hello, world!</b>
</message>"""


@app.route('/hello')
def hw():
    return 'hi'


def hw1():
    return 'hi'

app.add_url_rule('/helloko', 'helloko', hw1)


if __name__ == '__main__':
    app.run(debug = True)

