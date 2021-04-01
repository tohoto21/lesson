from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST','GET'])
def do_search() -> 'html':
    letters= request.form['letters']
    phrase= request.form['phrase']
    title= 'Here are your results:'
    results= str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title= title,
                           the_phrase= phrase,
                           the_letters= letters,
                           the_results= results,)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcom to search4letters on the web.')

if __name__ == '__main__':
    app.run( debug='True')