from abc import ABC, abstractmethod
from qiskit.aqua.utils.validation import validate_min
from qiskit.aqua.utils import CircuitFactory


class UncertaintyModel(CircuitFactory, ABC):
    """
    The abstract Uncertainty Model
    """

    __REPLACEMENT = 'a qiskit.QuantumCircuit'

    # pylint: disable=useless-super-delegation
    def __init__(self, num_target_qubits: int) -> None:
        validate_min('num_target_qubits', num_target_qubits, 1)
        super().__init__(num_target_qubits)

    @abstractmethod
    def build(self, qc, q, q_ancillas=None, params=None):
        raise NotImplementedError()
