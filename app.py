from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def Home():
    return "This is home page"

@app.route("/Welcome")
def welcome():
    return "This is flask tutorial"

@app.route("/index")
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)