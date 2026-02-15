from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/t/<token>')
def download_file(token):
    filename = f"{token}.pdf"
    return send_from_directory(
        directory='files',
        path=filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
