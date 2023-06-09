from flask import Flask, session

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1():
    return 'This is page 1.'


@app.route('/page2')
def page2():
    return 'This is page 2.'


@app.route('/page3')
def page3():
    return 'This is page 3.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return ' You are now logged in'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return "ypu are now logged out"

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return ' jdwa]iowda]iowad'
    return 'ipdakjip'

def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False

app.secret_key = 'YouWillNeverGuessMySecretKey'
if __name__ == '__main__':
    app.run(debug=True)
