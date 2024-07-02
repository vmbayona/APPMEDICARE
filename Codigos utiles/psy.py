import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from sklearn.utils import resample

# Ejemplo de dataset de síntomas y diagnósticos (se recomienda expandir este dataset en un entorno real)
data = {
    'symptoms': [
        'Me siento triste y sin esperanza', 
        'No puedo dormir bien por las noches', 
        'Tengo ataques de pánico frecuentes', 
        'Me siento ansioso y preocupado todo el tiempo', 
        'Tengo pensamientos suicidas', 
        'Me siento cansado y sin energía', 
        'No puedo concentrarme en nada', 
        'Tengo miedo de interactuar con otras personas',
        'Me siento irritado y con cambios de humor frecuentes',
        'He perdido interés en las actividades que antes disfrutaba'
    ],
    'diagnosis': [
        'Depresión', 
        'Insomnio', 
        'Trastorno de Pánico', 
        'Ansiedad Generalizada', 
        'Riesgo Suicida', 
        'Fatiga Crónica', 
        'Déficit de Atención', 
        'Fobia Social',
        'Trastorno Bipolar',
        'Anhedonia'
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Para este ejemplo, replicaremos las entradas para evitar las advertencias de métricas indefinidas
df_balanced = pd.concat([df] * 10, ignore_index=True)

# Separar características y etiquetas
X = df_balanced['symptoms']
y = df_balanced['diagnosis']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Crear el pipeline de TF-IDF y Naive Bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Entrenar el modelo
model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)

new_symptoms = input('Ingrese sintomas: ')

# Evaluar el modelo
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Función para predecir el diagnóstico basado en los síntomas
def predict_diagnosis(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]

# Ejemplo de uso
diagnosis = predict_diagnosis(new_symptoms)
print(f"Diagnóstico preliminar: {diagnosis}")
