from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['description']
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return jsonify({'RO': prediction})

if __name__ == '__main__':
    app.run(debug=True)
