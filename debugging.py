from flask import Flask
app = Flask(__name__)

@app.route('/')
def  hello_world():
    import pdb; pdb.set_trace() #execute line by line in vscode
    i = 3 
    i = i + 5 
    return "how are you" + str(i) + "times" 

if __name__ == '__main__':
    app.debug = True #it shows what is error 
    app.run()