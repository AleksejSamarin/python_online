import configparser
import os
from flask import Flask, json
from flask import render_template, request
from subprocess import PIPE, Popen
from subprocess import TimeoutExpired


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/launch', methods=['POST'])
def launch():
    code = injection + request.form['input_code']
    stdin = request.form['input_stdin']
    args = ['python', '-c', code, ",".join(banned_imports), ",".join(banned_functions)]

    process = Popen(args, **process_config)
    try:
        stdout, stderr = process.communicate(stdin, timeout)
    except TimeoutExpired:
        return json.dumps({'output': 'Timeout'})

    return json.dumps({'output': str(stdout) + str(stderr)})


def get_data_from_file(name):
    with open(os.path.join(path, f"./resources/{name}"), 'r') as file:
        return file.read()


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(path, './resources/config.ini'))
    process_config = {
        'stdin': PIPE,
        'stdout': PIPE,
        'stderr': PIPE,
        'encoding': config['process']['encoding']
    }
    timeout = float(config['process']['timeout'])
    banned_imports = ['os']
    banned_functions = ['open', 'exec', 'eval']
    injection = get_data_from_file('injection.txt')

    app.run(host='0.0.0.0', debug=True)
