{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from abc import ABC, abstractmethod\n",
    "from qiskit.aqua.utils.validation import validate_min\n",
    "from qiskit.aqua.utils import CircuitFactory\n",
    "\n",
    "\n",
    "class UncertaintyModel(CircuitFactory, ABC):\n",
    "    \"\"\"\n",
    "    The abstract Uncertainty Model\n",
    "    \"\"\"\n",
    "\n",
    "    __REPLACEMENT = 'a qiskit.QuantumCircuit'\n",
    "\n",
    "    # pylint: disable=useless-super-delegation\n",
    "    def __init__(self, num_target_qubits: int) -> None:\n",
    "        validate_min('num_target_qubits', num_target_qubits, 1)\n",
    "        super().__init__(num_target_qubits)\n",
    "\n",
    "    @abstractmethod\n",
    "    def build(self, qc, q, q_ancillas=None, params=None):\n",
    "        raise NotImplementedError()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
