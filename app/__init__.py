from flask import Flask,render_template,url_for,request,redirect
import os

app=Flask(__name__,template_folder='templates',static_folder='static')
UPLOADER_FOLDER='uploads'
app.secret_key='secrete it'
app.config['UPLOAD_FOLDER']=UPLOADER_FOLDER
# 30MB FIles size maximum
app.config['MAX_CONTENT_LENGHT']=30*1024*1024
@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

from app.views.uploader import uploader
app.register_blueprint(uploader)
@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
    print('going to upload file by choose')
    # return url_for('upload.home')
    return render_template('uploader.html')

@app.route('/files',methods=['GET','POST'])
def files():
    dados=request.form
    print(dados)
    if not dados:
        return render_template('files.html')
    else:
        return 'Dados found'
