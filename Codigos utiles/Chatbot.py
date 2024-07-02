import random
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Ejemplo de datos de entrenamiento
data = [
    ("Hola", "saludo"),
    ("Buenos días", "saludo"),
    ("Buenas tardes", "saludo"),
    ("Quiero agendar una cita", "agendar_cita"),
    ("Necesito una cita médica", "agendar_cita"),
    ("¿Puedo agendar una cita?", "agendar_cita"),
    ("Adiós", "despedida"),
    ("Hasta luego", "despedida"),
    ("Gracias", "agradecimiento"),
    ("Muchas gracias", "agradecimiento"),
]

# Preparar datos
X_train = [x[0] for x in data]
y_train = [x[1] for x in data]

# Convertir texto a vectores
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)

# Entrenar el modelo
clf = MultinomialNB()
clf.fit(X_train_vectors, y_train)

# Respuestas predefinidas
responses = {
    "saludo": ["Hola, ¿cómo puedo ayudarte?", "¡Hola! ¿En qué puedo asistirte hoy?"],
    "despedida": ["Adiós, ¡que tengas un buen día!", "Hasta luego, ¡cuídate!"],
    "agradecimiento": ["De nada, ¡siempre aquí para ayudar!", "¡A ti!"],
    "agendar_cita": ["Claro, ¿para qué especialidad te gustaría agendar la cita?"]
}

# Almacenar citas y estados de conversación
appointments = []
user_states = {}

# Configurar Flask
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.json.get('user_id', 'default')
    user_message = request.json.get('message')
    
    if user_id not in user_states:
        user_states[user_id] = {"stage": "initial"}
    
    user_stage = user_states[user_id]["stage"]
    
    if user_stage == "initial":
        user_message_vector = vectorizer.transform([user_message])
        prediction = clf.predict(user_message_vector)[0]
        
        if prediction == "agendar_cita":
            user_states[user_id]["stage"] = "awaiting_specialty"
            response = random.choice(responses[prediction])
        else:
            response = random.choice(responses[prediction])
    elif user_stage == "awaiting_specialty":
        user_states[user_id]["specialty"] = user_message
        user_states[user_id]["stage"] = "awaiting_doctor"
        response = "¿Con qué doctor te gustaría agendar la cita?"
    elif user_stage == "awaiting_doctor":
        user_states[user_id]["doctor"] = user_message
        user_states[user_id]["stage"] = "awaiting_date"
        response = "¿Para qué fecha te gustaría agendar la cita?"
    elif user_stage == "awaiting_date":
        user_states[user_id]["date"] = user_message
        user_states[user_id]["stage"] = "awaiting_time"
        response = "¿A qué hora te gustaría agendar la cita?"
    elif user_stage == "awaiting_time":
        user_states[user_id]["time"] = user_message
        specialty = user_states[user_id]["specialty"]
        doctor = user_states[user_id]["doctor"]
        date = user_states[user_id]["date"]
        time = user_message
        appointments.append({
            "user_id": user_id,
            "specialty": specialty,
            "doctor": doctor,
            "date": date,
            "time": time
        })
        response = (f"Tu cita con el Dr. {doctor} en {specialty} ha sido agendada para el {date} a las {time}. "
                    "¡Hasta luego, que tengas un buen día!")
        user_states[user_id]["stage"] = "initial"
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
