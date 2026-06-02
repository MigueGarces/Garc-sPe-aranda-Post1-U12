from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def oracle_constante(n: int):
    """
    Oráculo constante f(x)=0: no hace nada.
    """
    return QuantumCircuit(n + 1)

def oracle_balanceada(n: int):
    """
    Oráculo balanceado: aplica CNOT de cada qubit al ancilla.
    """
    qc = QuantumCircuit(n + 1)

    for i in range(n):
        qc.cx(i, n)

    return qc

def deutsch_jozsa(oracle_qc, n: int, shots: int = 1024):
    """
    Ejecuta Deutsch-Jozsa para un oráculo dado.
    """

    qc = QuantumCircuit(n + 1, n)

    # Preparar ancilla en |-> = H|1>
    qc.x(n)
    qc.h(range(n + 1))

    # Aplicar oráculo
    qc.compose(oracle_qc, inplace=True)

    # Interferencia
    qc.h(range(n))

    # Medir solo los qubits de entrada
    qc.measure(range(n), range(n))

    sim = AerSimulator()

    compiled = transpile(qc, sim)

    counts = sim.run(
        compiled,
        shots=shots
    ).result().get_counts()

    return counts

if __name__ == "__main__":

    n = 2

    # Caso constante
    counts_c = deutsch_jozsa(
        oracle_constante(n),
        n
    )

    print(f"Constante: {counts_c}")

    # Caso balanceado
    counts_b = deutsch_jozsa(
        oracle_balanceada(n),
        n
    )

    print(f"Balanceada: {counts_b}")

    assert "00" in counts_c, (
        "Error: oraculo constante no retorno 00"
    )

    assert "00" not in counts_b, (
        "Error: oraculo balanceado retorno 00"
    )

    print("OK: Deutsch-Jozsa verifica correctamente")