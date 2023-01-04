from flask import Flask, render_template, request
import xgboost as xgb
from flask_cors import CORS
import pickle
import numpy as np

import Universities
app = Flask(__name__)
CORS(app)


model_no = 0

modelFiles = Universities.filenames
unames = Universities.unames
print(modelFiles[0])

models = [None] * len(modelFiles)
models[0] = xgb.Booster()
models[0].load_model('./XGBoost_Models/' + modelFiles[0])
i = 0
for modelFile in modelFiles:
    models[i] = xgb.Booster({'nthread': 4})
    models[i].load_model('./XGBoost_Models/'+modelFile)
    i += 1



@app.route('/')
def index_supp():
    
    try:
        cgpa = float(request.args.get('cgpa'))
        quant = float(request.args.get('quant'))
        verbal = float(request.args.get('verbal'))
        toefl = float(request.args.get('toefl'))
        paper_pub = float(request.args.get('paper'))
        work_ex = float(request.args.get('work'))

        inpt = [[cgpa, quant, verbal, toefl, paper_pub, work_ex]]


        response = []
        ip = 0
        arr = xgb.DMatrix(inpt)
        for model in models:
            iuy = model.predict(arr).tolist()

            dct = {
                "University_names" : unames[ip],
                "Probabilty_of_acceptance" : abs(iuy[0]) * 100 
            }
            response.append(dct)
            ip+=1

        return response
    except Exception as err:
        print(err)
    return [1,2,3]
    
    # return render_template('home.html')

@app.route('/formdata')
def form_data():
    form_data = request.args
    cgpa = float(form_data['cgpa'])
    quant = float(form_data['quant'])
    verbal = float(form_data['verbal'])
    toefl = float(form_data['toefl'])
    paper_pub = float(form_data['paper_pub'])
    work_ex = float(form_data['work_ex'])



    # CGPA = float(request.form['CGPA'])
    # Quant = float(request.form['Quant'])
    # verbal = float(request.form['verbal'])
    # tofel = float(request.form['tofel'])
    # paper = float(request.form['paper'])
    # expr = float(request.form['expr'])
   
    # x = np.array([CGPA, Quant, verbal, tofel, paper, expr]).reshape(1, -1)

    inpt = [[cgpa, quant, verbal, toefl, paper_pub, work_ex]]
    return inpt

    arr = xgb.DMatrix(inpt)
    response = []
    ip = 0
    for model in models:
        iuy = model.predict(arr).tolist()

        dct = {
            "University names" : unames[ip],
            "Probabilty of acceptance" : abs(iuy[0]) * 100 
        }
        response.append(dct)
        ip+=1

    return response
    # return [0]


if __name__ == "__main__":
    app.run(debug=True, port=8000)