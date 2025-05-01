## Create a Simple flask application

from flask import Flask, render_template, request, redirect, url_for

## create a flask app

app = Flask(__name__)

@app.route('/')
def home():
    return "<i>Hello world</i>"

@app.route('/welcome')
def welcome():
    return "welcome to the flask tutorial"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return 'the person passed and the score is' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person failed and the score is' + str(score)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        average_marks = (maths+science+history)/3
        
        results=""
        
        if average_marks>50:
            results = 'success'
        else:
            results = 'fail'
            
        # return redirect(url_for(result, score=average_marks))    
        
        return render_template('result.html', results=average_marks)

if __name__=='__main__':
    app.run(debug=True)