from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('form.html')
    else: 
        almondFlour = 5
        return f"For {request.form['eggwhites']} {request.form['unit']} egg whites, you will need {almondFlour} {request.form['unit']} of almond flour."