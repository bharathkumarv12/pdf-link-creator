from flask import Flask, render_template_string, request, send_from_directory
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Upload & Link Generator</title>
</head>
<body style="font-family: Arial; padding:40px;">
    <h2>Upload PDF</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="pdf" accept="application/pdf" required>
        <br><br>
        <button type="submit">Upload</button>
    </form>

    {% if link %}
        <h3>Download Link:</h3>
        <a href="{{ link }}" target="_blank">{{ link }}</a>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    link = None
    if request.method == 'POST':
        file = request.files['pdf']
        if file:
            token = str(uuid.uuid4()).replace('-', '')[:10]
            filename = f"{token}.pdf"
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            link = f"http://127.0.0.1:5000/sevasindhuservices.karnataka.gov.in/{token}"

    return render_template_string(HTML_PAGE, link=link)

@app.route('/sevasindhuservices.karnataka.gov.in/<token>')
def download(token):
    filename = f"{token}.pdf"
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
