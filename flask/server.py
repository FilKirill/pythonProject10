from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
