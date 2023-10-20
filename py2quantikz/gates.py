class CircuitElement:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol
        self.quantikz_repr = None


    def __repr__(self) -> str:
        return self.symbol


    def set_quantikz_repr(self, repr: str) -> None:
        self.quantikz_repr = repr


    def get_quantikz_repr(self) -> str:
        return self.quantikz_repr


class QuantumGate(CircuitElement):
    def __init__(self, name: str, symbol: str) -> None:
        super().__init__(name, symbol)
        self.quantikz_repr = f"\\gate{{{self.symbol}}}"


class QuantumControlled(CircuitElement):
    def __init__(self, name: str, symbol: str, parameter: int) -> None:
        super().__init__(name, symbol)
        self.parameter = parameter
        self.quantikz_repr = f"\\ctrl{{{self.parameter}}}"


    def __repr__(self) -> str:
        return f"{self.symbol} to {self.parameter}"


H = QuantumGate("Hadamard", "H")
X = QuantumGate("Pauli-X", "X")
M = CircuitElement("Measurement", "M")
M.set_quantikz_repr("\\meter{}")