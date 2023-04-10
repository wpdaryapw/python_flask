from flask import Flask
from vsearch import  search4letters
from flask import Flask, render_template, request, escape
from DBcm import UseDatabase
app = Flask(__name__)
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '11111',
        'database': 'vsearchlogdb'
    }


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with UseDatabase (app.config['dbconfig']) as cursor:
        _SQL = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, str(req.user_agent), res, ))

@app.route('/search4', methods =['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '   Here are your result:'
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_phrase=phrase, the_leetters=letters,the_title=title,the_results=result,)
@app.route('/')

@app.route('/entry')
def entry_page() -> 'html':
    return  render_template('entry.html', the_title='Welcome to search4letters on the web!')
@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    title = ('Phrase', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_title=title, the_data=contents,)
if __name__=='__main__':
    app.run(debug=True)