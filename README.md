# py2quantikz

A library to convert Quantum code to LaTeX quantikz circuit diagrams.

## Installation

Install using `pip`:

```shell
pip install py2quantikz
```

## Usage

Initialize a circuit using `QuantumCircuit()` and pass in the number of qubits in the system.

Use the `apply()` method of `QuantumCircuit` to pass in a `GateApplication` or a list of `GateApplication` to it.

Get the circuit diagram code with the `quantikz()` method of `QuantumCircuit`.

```python
from py2quantikz.py2quantikz import QuantumCircuit, GateApplication as ga
import py2quantikz.gates as qg

circuit = QuantumCircuit(4)

circuit.apply([ga(qg.H, 0), ga(qg.H, 2)])
circuit.apply([ga(qg.X, 1, 0), ga(qg.X, 3, 2)])
circuit.apply([ga(qg.M, 0), ga(qg.M, 2)])

quantikz_repr = circuit.quantikz()
print(quantikz_repr)
```

This will result in

```latex
Q_0 & \gate{H} & \ctrl{1} & \meter{} & \\
Q_1 &          & \gate{X} &          & \\
Q_2 & \gate{H} & \ctrl{1} & \meter{} & \\
Q_3 &          & \gate{X} &          & \\
```

The `quantikz()` method accepts a separation parameter `sep`, which is used to separate the individual circuit elements.

```python
circuit.quantikz(sep="&[0.5em]")
```
