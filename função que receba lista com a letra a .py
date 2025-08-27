def palavras_com_a(lista):
    return sum(1 for palavras in lista if palavras.low().startwith("a"))
    print(palavras_com_a(["amor , vida"]))

