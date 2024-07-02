import speech_recognition as sr
import pyttsx3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Ejemplo de dataset de síntomas y diagnósticos
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

# Crear DataFrame y replicar datos para el ejemplo
df = pd.DataFrame(data)
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

# Predecir en el conjunto de prueba y evaluar el modelo
y_pred = model.predict(X_test)
#print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Configurar el reconocimiento de voz y el sintetizador de texto a voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para reconocer el habla y hacer un diagnóstico preliminar
def diagnose_from_speech():
    with sr.Microphone() as source:
        print("Por favor, describe tus síntomas...")
        speak("Por favor, describe tus síntomas...")
        audio = recognizer.listen(source)

        try:
            symptoms = recognizer.recognize_google(audio, language="es-ES")
            print(f"Usted dijo: {symptoms}")
            speak(f"Usted dijo: {symptoms}")

            # Aquí se usaría el modelo de diagnóstico
            diagnosis = predict_diagnosis(symptoms)
            print(f"Diagnóstico preliminar: {diagnosis}")
            speak(f"Diagnóstico preliminar: {diagnosis}")

        except sr.UnknownValueError:
            print("Lo siento, no pude entender lo que dijiste.")
            speak("Lo siento, no pude entender lo que dijiste.")
        except sr.RequestError:
            print("Error al conectarse al servicio de reconocimiento de voz.")
            speak("Error al conectarse al servicio de reconocimiento de voz.")

# Función para predecir el diagnóstico basado en los síntomas
def predict_diagnosis(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]

# Iniciar el reconocimiento de voz
diagnose_from_speech()
