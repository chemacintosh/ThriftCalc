import glob
import sys

from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import numpy

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:

    def __init__(self):
        self.log = {}

    def ping(self):
        print("me han hecho ping()")

    def suma(self, n1, n2):

        print("sumando " + str(n1) + " con " + str(n2))
        self.ans = n1 + n2
        return n1 + n2

    def resta(self, n1, n2):

        print("restando " + str(n1) + " con " + str(n2))
        self.ans = n1 - n2
        return n1 - n2

    def multiplicacion(self, n1, n2):
        self.ans = numpy.cross(n1, n2)

        print("multiplicando " + str(n1) + " con " + str(n2))
        return self.ans

    def division(self, n1, n2):

        print("Dividiendo " + str(n1) + " con " + str(n2))

        self.ans = numpy.divide(n1, n2)

        return self.ans

    def pow(self, n1, n2):
        print(str(n1) + " elevado a " + str(n2))
        self.ans = pow(n1, n2)

        return self.ans

    def raizCuadrada(self, n1, n2):
        print("Raiz " + str(n2) + " de " + str(n1))
        self.ans = pow(n1, 1.0/n2)

        return self.ans

    def sumaVector(self, v1, v2):
        print("Sumando " + str(v1) + " con " + str(v2))
        arr1 = numpy.array(v1)
        arr2 = numpy.array(v2)

        self.ans = arr1 + arr2
        return self.ans

    def restaVector(self, v1, v2):
        print("Restando " + str(v1) + " con " + str(v2))
        arr1 = numpy.array(v1)
        arr2 = numpy.array(v2)

        self.ans = arr1 - arr2
        return self.ans

    def multiVector(self, v1, v2):
        print("Multiplicando " + str(v1) + " con " + str(v2))
        arr1 = numpy.array(v1)
        arr2 = numpy.array(v2)

        self.ans = numpy.cross(arr1, arr2)
        return self.ans

    def divVector(self, v1, v2):
        print("Dividiendo " + str(v1) + " con " + str(v2))
        arr1 = numpy.array(v1)
        arr2 = numpy.array(v2)

        self.ans = numpy.divide(arr1, arr2)
        return self.ans

    def prodEscalar(self, v1, v2):
        print("Producto Escalar de " + str(v1) + " con " + str(v2))
        arr1 = numpy.array(v1)
        arr2 = numpy.array(v2)

        self.ans = arr1 @ arr2
        return self.ans


if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    server.serve()
    print("fin")
