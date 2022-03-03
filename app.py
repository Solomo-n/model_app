import flask
import pickle
import pandas as pd

with open("C:\\Users\HP\Desktop\FINAL YEAR PROJECT\SOFTWARE DEVELOPMENT\model_app\model\heart_disease_RF.pkl", 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        age = flask.request.form['age']
        sex = flask.request.form['sex']
        cp = flask.request.form['cp']
        trestbps = flask.request.form['trestbps']
        chol = flask.request.form['chol']
        fbs	= flask.request.form['fbs']
        restecg = flask.request.form['restecg']
        thalach = flask.request.form['thalach']
        exang = flask.request.form['exang']
        oldpeak = flask.request.form['oldpeak']
        slope = flask.request.form['slope']
        ca = flask.request.form['ca']
        thal = flask.request.form['thal']
        
        Diagnosis_one = "There is an 80% probability that you have a form of Heart Disease, and therefore advise that you visit the nearest healthcare location"
        Diagnosis_two = "There is an 80% probability that you do not have any heart disease."
        input_variables = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'], dtype=int)
        prediction = model.predict(input_variables)[0]

        if prediction == 0 :
            return flask.render_template('index.html', result = Diagnosis_two)
        else:
            return flask.render_template('index.html', result = Diagnosis_one)

if __name__ == '__main__':
    app.run()