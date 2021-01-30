# Code based on pythonbuddy.com

from flask import Flask, render_template, request, jsonify, session, redirect
import os

# Configure Flask App
# Remember to change the SECRET_KEY!
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/Users/juliadeng/src/codingchallenge/imageUploader/static/images'

@app.route('/')
def index():
    """Display home page
        :return: index.html
    """
    session["count"] = 0
    return render_template("index.html")

'''
BEGIN TASK 1
'''
# from flask documentation: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files

# Should you use a GET or POST Request?
@app.route('/submit_image', methods=['POST'])    
def submit_image():        #invoked when sent POST request
    """Adds an image to our server and adds it to our webpage. 
        Automatically refreshes our webpage so that user can see the image appended
    """
    # How do we store images in our server?
    # if request.files:
    print("hi")
    file = request.files['image_file']
    # if file.filename != '':
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    print("Image saved")
    # return redirect(request.url)
    return "whaa"
'''
END TASK 1
'''