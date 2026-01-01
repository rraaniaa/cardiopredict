from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    probability = None
    if request.method == 'POST':
        try:
            # Récupérer les valeurs importantes pour Heart Disease
            age = float(request.form['age'])
            cp = float(request.form['cp'])  # type de douleur thoracique
            thal = float(request.form['thal'])  # thalassémie
            ca = float(request.form['ca'])  # nombre de vaisseaux
            oldpeak = float(request.form['oldpeak'])
            chol = float(request.form['chol'])
            exang = float(request.form['exang'])
            slope = float(request.form['slope'])

            # Simulation réaliste basée sur les feature importance typiques
            risk_score = 0
            if thal == 7 or thal == 6: risk_score += 30
            if ca > 0: risk_score += 25
            if cp > 0: risk_score += 20
            if oldpeak > 1.5: risk_score += 18
            if chol > 240: risk_score += 15
            if age > 55: risk_score += 12
            if exang == 1: risk_score += 10
            if slope == 2: risk_score += 8

            probability = min(99, risk_score + random.randint(-10, 10))
            prediction = "Présence de maladie cardiaque" if probability > 50 else "Absence de maladie cardiaque"

        except:
            prediction = "Erreur dans les valeurs saisies"

    return render_template('index.html', prediction=prediction, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)