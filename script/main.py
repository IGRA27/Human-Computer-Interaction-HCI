import json

# Lee el archivo JSON
with open('emotions-n-i.txt', 'r') as file:
    data = json.load(file)

# Inicializa diccionarios para almacenar la suma de cada emoción y el recuento de muestras
sum_emotions = {"neutral": 0, "happy": 0, "sad": 0, "angry": 0, "fearful": 0, "disgusted": 0, "surprised": 0}
count = 0

# Suma las puntuaciones de cada emoción
for entry in data:
    for emotion, value in entry.items():
        sum_emotions[emotion] += value
    count += 1

# Calcula el promedio de cada emoción
average_emotions = {emotion: total / count for emotion, total in sum_emotions.items()}

# Imprime los promedios de cada emoción
for emotion, average in average_emotions.items():
    print(f"{emotion}: {average}")