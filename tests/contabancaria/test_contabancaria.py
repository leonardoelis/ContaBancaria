from io import StringIO
from contextlib import redirect_stdout


class TestContaBancaria:
    def test_depositar_valor_positivo(self, contas):
        conta1, _ = contas
        with redirect_stdout(StringIO()) as output:
            conta1.depositar(50)
        assert conta1.saldo == 150
        assert f"Depósito de R$50.00 realizado. Novo saldo: R${conta1.saldo:.2f}" in output.getvalue()

    def test_depositar_valor_negativo(self, contas):
        conta1, _ = contas
        with redirect_stdout(StringIO()) as output:
            conta1.depositar(-20)
        assert conta1.saldo == 100
        assert "Valor inválido para depósito. Depósito não realizado." in output.getvalue()

    def test_sacar_valor_positivo(self, contas):
        conta1, _ = contas
        with redirect_stdout(StringIO()) as output:
            conta1.sacar(50)
        assert conta1.saldo == 50
        assert f"Saque de R$50.00 realizado. Novo saldo: R${conta1.saldo:.2f}" in output.getvalue()

    def test_sacar_valor_acima_do_saldo(self, contas):
        conta1, _ = contas
        with redirect_stdout(StringIO()) as output:
            conta1.sacar(200)
        assert conta1.saldo == 100
        assert "Saldo insuficiente. Operação não realizada." in output.getvalue()

    def test_sacar_valor_negativo(self, contas):
        conta1, _ = contas
        with redirect_stdout(StringIO()) as output:
            conta1.sacar(-20)
        assert conta1.saldo == 100
        assert "Valor inválido para saque. Saque não realizado." in output.getvalue()

    def test_transferir_valor_positivo(self, contas):
        conta1, conta2 = contas
        with redirect_stdout(StringIO()) as output:
            conta1.transferir(conta2, 50)
        assert conta1.saldo == 50
        assert conta2.saldo == 100
        assert f"Transferencia de R$50.00 realizada. Novo saldo: R${conta1.saldo:.2f}" in output.getvalue()

    def test_transferir_valor_acima_do_saldo(self, contas):
        conta1, conta2 = contas
        with redirect_stdout(StringIO()) as output:
            conta1.transferir(conta2, 200)
        assert conta1.saldo == 100
        assert conta2.saldo == 50
        assert "Saldo insuficiente. Transferência nào realizada." in output.getvalue()

    def test_transferir_valor_negativo(self, contas):
        conta1, conta2 = contas
        with redirect_stdout(StringIO()) as output:
            conta1.transferir(conta2, -50)
        assert conta1.saldo == 100
        assert conta2.saldo == 50
        assert "Valor inválido para transferência. Transferência nào realizada." in output.getvalue()