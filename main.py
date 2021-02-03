import os
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from calc import Calculation

app = Flask(__name__)
app.secret_key = "12ffa78io?rf891iflol007f"

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(f'/calc/{filename[:-4]}')
    else:
        flash('Allowed file types are txt')
        return redirect(request.url)


@app.route("/calc/<filename>")
def calc(filename):
    return render_template("calc.html")


@app.route("/calc/<filename>", methods=['GET', 'POST'])
def calculate_values(filename):

    if request.method == 'POST':
        with open(f"{app.config['UPLOAD_FOLDER']}/{filename}.txt", "r") as f:
            num_list = []
            for line in f:
                line = line.strip('\n')
                if len(line) == 1:
                    if line.isdigit():
                        num_list.append(int(line))
                else:
                    if line[1:].isdigit() and (line[0] == '-' or line[0].isdigit()):
                        num_list.append(int(line))
        calc = Calculation(num_list)
        calculate_message = {'Maximum value in a file: ': calc.max_number(),
                             'Minimum value in a file: ': calc.min_number(),
                             'Median: ': calc.median(),
                             'Arithmetic mean: ': calc.average(),
                             'Longest subsequence of increasing values in an array: ': calc.ascending_sequence(),
                             'Longest subsequence of decreasing values in an array: ': calc.descending_sequence()
                             }
        for key, value in calculate_message.items():
            flash(f'{key}{value}')
        os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}.txt")
        return redirect(request.url)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
