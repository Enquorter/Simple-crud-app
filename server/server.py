# server.py
from flask import Flask, request
import os

filePath = "data.txt"

app = Flask(__name__)

# Display text 
@app.route('/data.txt', methods=['GET'])
def get_data():
    if(os.path.isfile(filePath)==False):
        return "The file doesnt exist"
    file = open(filePath, "r+")
    text = file.read()
    file.close()
    return text

# Create a file
@app.route('/data.txt', methods=['POST'])
def post_data():
    if(os.path.isfile(filePath)):
        return "The file already exists"
    file = open(filePath, "w+")
    file.close()
    return "File was created"

# Delete text and add new 
@app.route('/data.txt', methods=['PUT'])
def replace_data():
    file = open(filePath, "w")
    text = request.data.decode("utf-8")
    file.write(text)
    file.close()
    return "File was changed"

# Add new text
@app.route("/data.txt", methods=['PATCH'])
def update_data():
    file = open(filePath, "a+")
    text = request.data.decode("utf-8")
    file.write('\n'+text)
    file.close()
    return "File was edited"

# Delete a file
@app.route('/data.txt', methods=['DELETE'])
def delete_data():
    os.remove(filePath)
    return "File removed"

# Can't run it using port 3000
app.run(port=5000)