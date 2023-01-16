from flask import Blueprint,render_template,abort,request,url_for,redirect
from werkzeug.utils import secure_filename
import os


uploader=Blueprint('upload',__name__,url_prefix='/upload')
from app import app
@uploader.route('/',methods=['POST','GET'])
def home():
    # data=request.files['first_file'] #pega so o primeiro file
    # try:
    data=request.files.getlist("first_files")
    frm=request.form
    for file in data:
        print(file)
        EXIST=os.path.exists(app.config['UPLOAD_FOLDER'])
        print(app.config['UPLOAD_FOLDER'],EXIST)
        print(type(file))
        if EXIST:
            file_name=secure_filename(file.filename)
            full_path=os.path.join(app.config['UPLOAD_FOLDER'],file_name)
            print(full_path)
            file.save(full_path)
        print('saved sucessfule')
    
    # except Exception as e:
    #     return f'ERROR\t {e}'
    return redirect(url_for('upload_file'))