from flask import Flask 

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello world' 

@app.route('/greeting/<name>')
def greet(name):
    return "hello " + str(name) + " How r u" 

@app.route('/marks/<marks>')
def name_marks(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"



if __name__ == '__main__':
    app.run()
