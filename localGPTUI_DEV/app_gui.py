from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Check if it's a PDF and print the number of pages
        if filename.rsplit('.', 1)[1].lower() == 'pdf':
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)  # Using PdfReader
                number_of_pages = len(pdf_reader.pages)   # Get number of pages
                print(f"The uploaded PDF has {number_of_pages} pages.")

        return redirect(url_for('uploaded_file', filename=filename))
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)

