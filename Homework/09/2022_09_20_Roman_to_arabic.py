def roman_converter(in_str):
    """
    Функция перевода римских чисел в арабские.
    :param in_str: входная строка с римскими числами (строка).
    :return: возвращаем арабское число (int).
    """
    alph = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}

    output = alph[in_str[0]]

    for i in range(1, len(in_str)):
        if alph[in_str[i]] <= alph[in_str[i-1]]:
            output += alph[in_str[i]]
        else:
            output = output - 2 * alph[in_str[i-1]] + alph[in_str[i]]

    return output


if __name__ == "__main__":
    # Тесты для функции
    assert 5 == roman_converter("V")
    assert 15 == roman_converter("XV")
    assert 19 == roman_converter("XIX")
    assert 60 == roman_converter("LX")
    assert 150 == roman_converter("CL")
    assert 4 == roman_converter("IV")
    assert 40 == roman_converter("XL")
    assert 9 == roman_converter("IX")
    assert 80 == roman_converter("LXXX")
    assert 90 == roman_converter("XC")
    assert 1950 == roman_converter("MCML")
    assert 2325 == roman_converter("MMCCCXXV")
    assert 2550 == roman_converter("MMDL")
    assert 2544 == roman_converter("MMDXLIV")
    assert 89 == roman_converter("LXXXIX")