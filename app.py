from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

# Base cargada internamente
df = pd.read_excel("BASE-CONCURSO.xlsx")
df.columns = df.columns.str.strip()

@app.route('/')
def index():
    # Enviar los IDs disponibles al frontend
    ids_list = df['ID'].tolist()
    return render_template('index.html', ids=ids_list)

@app.route('/sortear')
def sortear():
    ganador = df.sample().iloc[0]
    return jsonify({
        "ID": int(ganador["ID"]),
        "Nombre": str(ganador["Nombre"]),
    })

@app.route('/health')
def salud():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
