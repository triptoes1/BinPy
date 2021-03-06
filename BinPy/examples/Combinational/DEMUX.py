from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for DEMUX class """
print ("\n---Initializing the DEMUX class--- ")
print ("demux = DEMUX(1) #Must be a single input")
demux = DEMUX(1)
print ("\n---Put select lines---")
print ("demux.selectLines(0) #Select Lines must be power of 2")
demux.selectLines(0)
print ("\n---Output of demux")
print ("demux.output()")
print (demux.output())
print ("\n---Input changes---")
print ("demux.setInput(0, 0) #Input at index 1 is changed to 0")
demux.setInput(0, 0)
print ("\n---New Output of the demux---")
print (demux.output())
print ("\n---Get Input States---")
print ("demux.getInputStates()")
print (demux.getInputStates())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output of demux to Connector conn---")
print ("demux.setOutput(0, conn) #sets conn as the output at index 0")
demux.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
print ("\n---Changing select lines---")
print ("demux.selectLine(0, 1) #selects input line 2")
demux.selectLine(0, 1)
print ("---New output of demux---")
print (demux.output())
