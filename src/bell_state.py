from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def bell_state_experiment(shots: int = 1024):
    """
    Prepara el estado de Bell |Φ+> y mide los dos qubits.
    """

    # Crear circuito con 2 qubits y 2 bits clásicos
    qc = QuantumCircuit(2, 2)

    # Paso 1: crear superposición en el primer qubit
    qc.h(0)

    # Paso 2: entrelazar con CNOT
    qc.cx(0, 1)

    # Paso 3: medir ambos qubits
    qc.measure([0, 1], [0, 1])

    # Simulador
    simulator = AerSimulator()

    # Compilar circuito
    compiled = transpile(qc, simulator)

    # Ejecutar simulación
    job = simulator.run(compiled, shots=shots)

    # Obtener resultados
    counts = job.result().get_counts()

    print(f"Resultados Bell |Φ+> ({shots} shots):")

    for state, count in sorted(counts.items()):
        pct = count / shots * 100
        print(f" |{state}> : {count:4d} ({pct:.1f}%)")

    # Verificación esperada: solo 00 y 11
    assert "01" not in counts and "10" not in counts, (
        "ERROR: aparecieron estados no entrelazados"
    )

    print("OK: correlación perfecta verificada")

    # Guardar histograma
    fig = plot_histogram(counts)
    fig.savefig(
        "capturas/bell_histogram.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close(fig)

    print("\nDiagrama del circuito:")
    print(qc.draw())

    return counts


if __name__ == "__main__":
    bell_state_experiment()