# Função 1 – Inverter string
def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    input_str = "TripleTen"
    reversed_str = reverse_string(input_str)
    assert reversed_str == "neTelpirT"
    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)


# Função 2 – Verificar palíndromo
def is_palindrome(word):
    return word == ''.join(reversed(word))

def test_is_palindrome():
    input_str = "osso"
    result = is_palindrome(input_str)
    assert result is True
    print("Teste aprovado! '" + input_str + "' é um palíndromo.")


# Função 3 – Calcular fatorial
import math

def compute_factorial(number):
    return math.factorial(number)

def test_compute_factorial():
    input_number = 5
    result = compute_factorial(input_number)
    assert result == 120
    print("Teste aprovado! O fatorial de", input_number, "é", result)
