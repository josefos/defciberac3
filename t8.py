import os
from flask import Flask, jsonify, request
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
