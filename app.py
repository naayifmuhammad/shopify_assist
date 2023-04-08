from flask import Flask, render_template, redirect, request

app = Flask(__name__)


class User:
    def __init__(self,name):
        self.name = name

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/<name>',)
def run(name):
    user = User(name)
    return render_template('dashboard.html')


if __name__=='__main__':
    app.run()