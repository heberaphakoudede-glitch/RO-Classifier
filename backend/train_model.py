import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Charger le dataset
data = pd.read_csv('incidents.csv')  # colonnes: description, RO
X = data['description']
y = data['RO']

# Vectorisation
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Entraînement du modèle
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Sauvegarde
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
