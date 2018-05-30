from flask import Flask, request, redirect, render_template, session
from scripts.load_file import *
from scripts.send_gmail import *

app = Flask(__name__)
app.secret_key = 'koto'

@app.route('/', methods=['GET'])
def top():
    params = {}
    params['programs'] = get_program_all()
    return render_template('index.html', params=params)

@app.route('/<program_keyname>/input', methods=['GET'])
def input(program_keyname=None):
    program = get_program('./program-data/%s' % program_keyname + '.json')

    params = {}
    params['program'] = program
    session['program'] = program

    return render_template('program/input.html', params=params)

@app.route('/<program_keyname>/confirm', methods=['POST'])
def confirm(program_keyname=None):
    if request.method == 'POST':
        program = session.get('program')
        for corner in program['corners']:
            if corner['keyname'] == request.form['corner']:
                corner_name = corner['name']

        params = {}
        params['program_name'] = program['name']
        params['program_keyname'] = program['keyname']
        params['corner'] = corner_name
        params['radio_name'] = request.form['radio-name']
        params['email'] = request.form['email']

        return render_template('program/confirm.html', params=params) 

@app.route('/<program_keyname>/send', methods=['POST'])
def send(program_keyname=None):
    if request.method == 'POST':
        program = session.get('program')
        post_params = request.form
        for param in post_params:
            print(param)

        try:
            result = do_send(program)
        except Exception as e:
            print(e)
            exit()

        if result:
            return render_template('program/send.html')

if __name__ == '__main__':
    app.run(debug=True)
