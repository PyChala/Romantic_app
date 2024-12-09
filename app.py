"""A romantic web app to propose to your crush."""
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def manifesto():
    """Renders the manifesto template"""
    return render_template('manifesto.html')

@app.route('/proposal')
def proposal():
    """Renders the proposal template."""
    return render_template('proposal.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Logs the response to the proposal"""
    choice = request.form['choice']
    with open('choices.txt', 'a', encoding='utf-8') as f:
        f.write(f'{choice}\n')
    if choice == 'yes':
        feedback = 'Yay🥳🥳🥳. I will the best man you will ever have.'
    else:
        feedback = 'Aight. Not meant to be I guess. You will always be my love.'
    return render_template('proposal.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
