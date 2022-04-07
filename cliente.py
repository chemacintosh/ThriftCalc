from array import array
from tokenize import Double
from unittest import case, result
from calculadora import Calculadora
import numpy
from array import array

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

transport.open()

print("hacemos ping al server")
client.ping()
terminado = False
print("Bienvenido a la calculadora\n")

while True:
    print("¿Desea realizar operaciones con vectores?(s/n): ")
    resp = input()
    if resp == "n":
        print("Ingrese el primer valor: ")
        n1 = float(input())

        print(
            "Ingrese el signo de la operacion ('+', '-', '*', '/', 'raiz', 'elevado a'): ")
        signo = input()

        print("Ingrese el segundo valor: ")
        n2 = float(input())

        if signo == "+":
            resultado = client.suma(n1, n2)
        elif signo == "-":
            resultado = client.resta(n1, n2)
        elif signo == "*":
            resultado = client.multiplicacion(n1, n2)
        elif signo == "/":
            resultado = client.division(n1, n2)
        elif signo == "raiz":
            resultado = client.raizCuadrada(n1, n2)
        elif signo == "elevado a":
            resultado = client.pow(n1, n2)

    else:
        print("Ingrese uno a uno los numeros del primer vector ('stop' para dejar de escribir): ")
        n1 = []
        while True:
            resp = input()
            if resp != "stop":
                n1.append(float(resp))
            else:
                break

        print("Ingrese el signo de la operacion ('+', '-', '*', '/', '| prod escalar'): ")
        signo = input()

        print("Ingrese uno a uno los numeros del segundo vector ('stop' para dejar de escribir): ")
        n2 = []
        while True:
            resp = input()
            if resp != "stop":
                n2.append(float(resp))
            else:
                break

        if signo == "*":
            resultado = client.multiVector(n1, n2)
        elif signo == "/":
            resultado = client.divVector(n1, n2)
        if signo == "+":
            resultado = client.sumaVector(n1, n2)
        elif signo == "-":
            resultado = client.restaVector(n1, n2)
        elif signo == "|":
            resultado = client.prodEscalar(n1, n2)

    print("El resultado de " + str(n1) + " " +
          signo + " " + str(n2) + " = " + str(resultado))

    print("\n¿Desea realizar otra operacion?(s/n): ")
    if input() == "n":
        break


transport.close()
