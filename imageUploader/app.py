# Code based on pythonbuddy.com

from flask import Flask, render_template, request, jsonify, session

UPLOAD_FOLDER = 'C:/uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Configure Flask App
# Remember to change the SECRET_KEY!
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Should you use a GET or POST Request?
@app.route('/submit_image', methods=['POST'])    
def submit_image():        #invoked when sent POST request
    """Adds an image to our server and adds it to our webpage. 
        Automatically refreshes our webpage so that user can see the image appended
    """
    # How do we store images in our server?
    file = request.files['file']
    # if allowedfile(file.filename)
    if file.filename != '':
        file.save(app.config['UPLOAD_FOLDER'], + file.filename)
    return render_template("index.html") 
'''
END TASK 1
'''