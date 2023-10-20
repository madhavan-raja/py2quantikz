from py2quantikz.py2quantikz import QuantumCircuit, GateApplication as ga
import py2quantikz.gates as qg

circuit = QuantumCircuit(4)

circuit.apply([ga(qg.H, 0), ga(qg.H, 2)])
circuit.apply([ga(qg.X, 1, 0), ga(qg.X, 3, 2)])
circuit.apply([ga(qg.M, 0), ga(qg.M, 2)])

quantikz_repr = circuit.quantikz(sep="&[0.5em]")
print(quantikz_repr)