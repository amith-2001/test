from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-image', methods=['POST'])
def fetch_image():
    url = "your_mongodb_connection_string"
    client = MongoClient(url)
    db = client['ImageDB']
    collection = db['Images']
    image_id = '669384c29d641b645995cd89'
    image_document = collection.find_one({'_id': ObjectId(image_id)})

    if image_document and 'image' in image_document:
        with open('output_image.png', 'wb') as f:
            f.write(image_document['image'])
        return "Image fetched and written to 'output_image.png'"
    else:
        return "Image not found in the database"

if __name__ == '__main__':
    app.run(debug=True)
