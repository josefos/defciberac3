import os
from flask, import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.router('/')
def nao_entre_em_panico():

    limite = 100

    c = 1
    p = 1
    numero = 3

    primos = "2,"

    while p < limite:
       ehprimo = 1
        for i in rang(2, numero):
            if numero % i == 0:
                ehprimo =0
                break
        if (ehprimo)
            primos = primos + str(numero) + ","
            p =+ 1
            if (p % 10 == 0):
                primos = primos + "<br>"
        numero+=1

    return

if __name__ == "__main__"
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



