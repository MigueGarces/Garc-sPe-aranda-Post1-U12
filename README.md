# Laboratorio Post-Contenido 1 – Unidad 12: Computación Emergente y Tendencias

## Autor

Miguel Ángel Garcés Peñaranda - 1152432

## Descripción

Este repositorio contiene la solución del laboratorio correspondiente a la Unidad 12: Computación Emergente y Tendencias.

El objetivo principal de la práctica es implementar y analizar tres algoritmos fundamentales de computación cuántica utilizando Python, Qiskit y AerSimulator:

- Estado de Bell
- Algoritmo de Deutsch-Jozsa
- Algoritmo de Grover para 2 qubits

Todos los experimentos fueron ejecutados mediante simulación local utilizando Qiskit Aer, sin emplear hardware cuántico real.

---

# Objetivos

## Objetivo general

Implementar y analizar circuitos cuánticos básicos mediante Qiskit para comprender conceptos fundamentales de la computación cuántica como superposición, entrelazamiento, interferencia y amplificación de amplitudes.

## Objetivos específicos

- Construir un estado de Bell y verificar el entrelazamiento cuántico.
- Implementar el algoritmo de Deutsch-Jozsa para distinguir funciones constantes y balanceadas.
- Implementar el algoritmo de Grover para encontrar estados objetivo en un espacio de búsqueda de dos qubits.
- Interpretar los histogramas generados por las mediciones cuánticas.
- Documentar el proceso mediante Git y GitHub.

---

# Experimento 1: Estado de Bell

## Fundamento teórico

El estado de Bell es uno de los ejemplos más simples de entrelazamiento cuántico.

El circuito se construye aplicando:

1. Una puerta Hadamard al primer qubit.
2. Una puerta CNOT utilizando el primer qubit como control.

## Resultado esperado

Al ejecutar 1024 mediciones, únicamente deben aparecer los estados:

```text
00
11
```

---

# Experimento 2: Algoritmo de Deutsch-Jozsa

## Fundamento teórico

El algoritmo de Deutsch-Jozsa permite determinar si una función es:

- Constante
- Balanceada

utilizando una única evaluación del oráculo.

Clásicamente serían necesarias varias consultas para llegar a la misma conclusión.

---

## Resultado esperado

### Caso constante

```text
Constante: {'00': 1024}
```

### Caso balanceado

```text
Balanceada: {'11': 1024}
```

También podrían aparecer:

```text
{'01': 1024}
```

o

```text
{'10': 1024}
```

Lo importante es que no aparezca:

```text
00
```

---

# Experimento 3: Algoritmo de Grover

## Fundamento teórico

El algoritmo de Grover permite encontrar un elemento dentro de un conjunto no estructurado utilizando menos operaciones que un algoritmo clásico.

Para dos qubits existen cuatro posibles estados:

```text
00
01
10
11
```

El objetivo consiste en amplificar la probabilidad de uno de ellos.

---

## Fases del algoritmo

### 1. Superposición

Se generan simultáneamente todos los estados posibles mediante puertas Hadamard.

### 2. Oráculo

Se marca el estado objetivo mediante un cambio de fase.

### 3. Difusor

Amplifica la amplitud del estado marcado.

---

## Casos evaluados

### Objetivo 00

Resultado esperado:

```text
Estado más probable: |00>
```

---

### Objetivo 01

Resultado esperado:

```text
Estado más probable: |01>
```

---

### Objetivo 10

Resultado esperado:

```text
Estado más probable: |10>
```

---

### Objetivo 11

Resultado esperado:

```text
Estado más probable: |11>
```

---

# Conclusiones

La práctica permitió implementar y analizar tres algoritmos fundamentales de la computación cuántica.

El experimento del Estado de Bell evidenció el fenómeno de entrelazamiento cuántico mediante correlaciones perfectas entre dos qubits.

El algoritmo de Deutsch-Jozsa demostró cómo la interferencia cuántica permite distinguir funciones constantes y balanceadas con una sola evaluación del oráculo.

Finalmente, el algoritmo de Grover mostró el proceso de amplificación de amplitudes para aumentar la probabilidad de encontrar un estado objetivo dentro de un espacio de búsqueda.

Estos experimentos permitieron comprender conceptos fundamentales de la computación cuántica utilizando simulación local con Qiskit.

---
