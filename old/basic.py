from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/algo/<name>')
def get_algo_name(name):
    return render_template('algo.html', name=name)


@app.route('/')
def get_basic():
    user_logged_in=True
    input_algorithm='linear regression'
    sq_foot=[11,35,13,45]
    input_dict = {'algorithm': 'linear regression'}
    input_values=list(sq_foot)
    return render_template('basic.html', input_algorithm=input_algorithm, input_values=input_values, \
                           input_dict=input_dict,sq_foot=sq_foot, user_logged_in=user_logged_in)


if __name__ == '__main__':
    app.run(port=8080, debug=True)