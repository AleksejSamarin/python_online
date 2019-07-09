import sys
from flask import Flask, json
from flask import render_template, request
from io import StringIO


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/launch', methods=['POST'])
def launch():
    code = request.form['input_code']
    stdin = request.form['input_stdin']

    old_stdin = None
    if code:
        old_stdout = sys.stdout
        if stdin:
            old_stdin = sys.stdin
            sys.stdin = StringIO(stdin)
        redirected_output = sys.stdout = StringIO()
        exec(code)
        sys.stdout = old_stdout
        if stdin:
            sys.stdin = old_stdin

        # print(code, stdin)
        return json.dumps({'output': redirected_output.getvalue()})


if __name__ == '__main__':
    app.run(debug=True)
