from flask import Blueprint, render_template, request, send_file, current_app, redirect, url_for
import os
from .utils import encrypt_file, decrypt_file, list_files

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename:
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            encrypt_file(uploaded_file, filepath)
    files = list_files(current_app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@main.route('/download/<filename>')
def download(filename):
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    decrypted_path = decrypt_file(filepath)
    return send_file(decrypted_path, as_attachment=True)

