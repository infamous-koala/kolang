from src.ext import Ext
from src.interpreter import BasicEval, BasicIntegration
import sys

filename = sys.argv[1]
Ext()

file = open(filename,"r")  
reader = file.read()

# basic eval
try:
    for i in reader:
        if i[0] in ["1","2","3","4","5","6","7","8","9","0"]:
            print(BasicEval(reader))

# Integration
        elif i[0] == "I" or i[0] == "i":
            print(BasicIntegration(reader))
except:
    print("[!] INVALID SYNTAX")
