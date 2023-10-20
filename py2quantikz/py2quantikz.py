from py2quantikz.gates import CircuitElement, QuantumControlled


class GateApplication:
    def __init__(self, gate: CircuitElement, targ: int, ctrl: (None | int | list) = None) -> None:
        if ctrl is None:
            ctrl = list()
        elif isinstance(ctrl, int):
            ctrl = [ctrl]

        self.gate = gate
        self.targ = targ
        self.ctrl = ctrl


    def __repr__(self) -> str:
        return f"{self.gate.symbol} at {self.targ} from {self.ctrl}"


class QuantumCircuit:
    circuit = list()


    def __init__(self, qubits):
        self.qubits = qubits


    def __repr__(self) -> str:
        return f"QuantumCircuit({self.circuit})"


    def apply(self, applications: GateApplication | list) -> None:
        if isinstance(applications, GateApplication):
            applications = [applications]

        self.circuit.append(applications)


    def generate_quantikz_list(self) -> list:
        quantikz_list = list()

        for gates in self.circuit:
            current = list([None for _ in range(self.qubits)])

            for application in gates:
                current[application.targ] = application.gate

                for ctrl in application.ctrl:
                    current[ctrl] = QuantumControlled("Target", "T", application.targ - ctrl)

            quantikz_list.append(current)

        return quantikz_list

    
    def generate_row_major(self) -> list:
        quantikz_list = self.generate_quantikz_list()
        row_major = list()

        for qubit in range(self.qubits):
            current = list()
            for timeline in quantikz_list:
                current.append(timeline[qubit])
            row_major.append(current)

        return row_major


    def generate_max_lens(self) -> list:
        quantikz_list = self.generate_quantikz_list()
        max_lens = list()

        for timeline in quantikz_list:
            max_len = 0

            for element in timeline:
                res = '' if element is None else element.get_quantikz_repr()

                max_len = max(max_len, len(res))

            max_lens.append(max_len)

        return max_lens

    
    def quantikz(self, sep: str = "&") -> str:
        row_major = self.generate_row_major()
        max_lens = self.generate_max_lens()

        res = str()

        for qubit, row in enumerate(row_major):
            res += f"Q_{str(qubit).zfill(len(str(self.qubits)))} {sep} "

            for i, element in enumerate(row):
                cur = '' if element is None else element.get_quantikz_repr()
                if len(cur) < max_lens[i]:
                    cur += " " * (max_lens[i] - len(cur))

                res += cur
                res += f" {sep} "

            res += "\\\\\n"

        return res