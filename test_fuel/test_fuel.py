from fuel import convert, gauge
import pytest


def main():
    test_divisao_por_zero()
    test_valor_invalido()
    test_saida_correta()


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_valor_invalido():
    with pytest.raises(ValueError):
        convert("gato/cachorro")


def test_saida_correta():
    # Teste com resultado esperado 25%
    resultado = convert('1/4')
    assert resultado == 25, f"Erro: conversão incorreta. Resultado: {resultado} | Esperado: 25"
    resultado_gauge = gauge(resultado)
    assert resultado_gauge == '25%', f"Erro: gauge incorreto. Resultado: {resultado_gauge} | Esperado: 25%"

    # Teste com resultado esperado E
    resultado = convert('1/100')
    assert resultado == 1, f"Erro: conversão incorreta. Resultado: {resultado} | Esperado: 1"
    resultado_gauge = gauge(resultado)
    assert resultado_gauge == 'E', f"Erro: gauge incorreto. Resultado: {resultado_gauge} | Esperado: E"

    # Teste com resultado esperado F
    resultado = convert('99/100')
    assert resultado == 99, f"Erro: conversão incorreta. Resultado: {resultado} | Esperado: 99"
    resultado_gauge = gauge(resultado)
    assert resultado_gauge == 'F', f"Erro: gauge incorreto. Resultado: {resultado_gauge} | Esperado: F"


if __name__ == "__main__":
    main()
