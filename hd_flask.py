from flask import Flask, request, render_template
from Hdisease import hdisease

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp_upload'

def hd_predict(age: float, sex: float, cp: float, trestbps: float , chol: float , fbs: float , restecg: float, thalach: float, exang: float, oldpeak: float, slope: float, ca: float, thal: float) -> str:
    hd = hdisease.theNet()
    predition = hd.predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    return predition

@app.route("/hdisease",methods=["GET","POST"])
def hd_controller():
    if request.method=='POST':
        age = float(request.form.get('age'))
        sex = float(request.form.get('sex'))
        cp = float(request.form.get('cp'))
        trestbps = float(request.form.get('trestbps'))
        chol = float(request.form.get('chol'))
        fbs = float(request.form.get('fbs'))
        restecg = float(request.form.get('restecg'))
        thalach = float(request.form.get('thalach'))
        exang = float(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = float(request.form.get('slope'))
        ca = float(request.form.get('ca'))
        thal = float(request.form.get('thal'))
        
        prediction = hd_predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return prediction
    return render_template("hd.html")

app.run(host="127.0.0.1",port=5000,debug=True)