from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

simulator = AerSimulator()

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1000)

result = job.result()
counts = result.get_counts()

flavors = {'0': 'Vanilla', '1': 'Chocolate'}

flavor_counts = {
    flavors[key]: value for key, value in counts.items()
}

plt.bar(flavor_counts.keys(), flavor_counts.values())

plt.xlabel('Ice Cream Flavor')
plt.ylabel('Counts')
plt.title('Quantum Ice Cream Distribution')

plt.show()