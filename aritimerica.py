nota_1= 0
nota_2= 0
nota_3= 0
nota_4= 0

def entrada_valores():
    global nota_1, nota_2, nota_3, nota_4
    nota_1 = float(input("entra com a nota 1:"))
    nota_2 = float(input("entra com a nota 2:"))
    nota_3 = float(input("entra com a nota 3:"))
    nota_4 = float(input("entra com a nota 4:"))

soma=0
def soma_valores():
    global nota_1, nota_2, nota_3, nota_4, soma
    soma=nota_1+nota_2+nota_3+nota_4


resultado=0
def divisao_valores():
    global soma, resultado
    resultado=soma/4

def exibir_valores():
    global resultado
    mensagem = f"a suamedia e igual {resultado}"
    print(mensagem)

entrada_valores()
soma_valores()
divisao_valores()
exibir_valores()












