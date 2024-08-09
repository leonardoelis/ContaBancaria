import pytest
from contaBancaria import ContaBancaria


@pytest.fixture
def contas():
    conta1 = ContaBancaria(100)
    conta2 = ContaBancaria(50)
    return conta1, conta2