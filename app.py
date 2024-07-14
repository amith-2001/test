import tempfile
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/fetch')
def hello_world():
   # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
       #temp_file.write(b'Hello, World!')
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)
