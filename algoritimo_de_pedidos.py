# Lista para cardápio [código_do_produto, nome_do_produto, preço]:
produtos = [[100, "cachorro-quente", 4.50], [101, "Hamburger", 5.00], [102, "Misto", 2.75], [103, "Refrigerante", 3.50]]

#lista produtos comprados
preço_produtos_comprados = []
nome_produtos_comprados = []

# Função de verificar se o código digitado corresponde a um produto:
def buscar_produtos():
    encontrar = 0
    for x in produtos:
        if codigo_digitado == x[0]:
            print(x[1])
            encontrar = 1
            if encontrar != 1:
                print("Código inválido")

# Função adicionar preço na lista de preços dos produtos comprados: 
def adicionar_preço():
    for x in produtos:
        if codigo_digitado == x[0]:
            preço = x[2]
            preço_produtos_comprados.append(x[2])

# Função adicionar nome dos produtos comprados na respectiva lista:
def adicionar_nomes():
    for x in produtos:
        if codigo_digitado == x[0]:
            nome = x[1]
            nome_produtos_comprados.append(x[1])

#primeiro pedido:
codigo_digitado = int(input("Código do produto: "))
buscar_produtos()
adicionar_preço()
adicionar_nomes()
adicionar_algo = input("Deseja adicionar algo mais? ")

#Quando quiser adicionar mais pedidos
while adicionar_algo == "sim":
    codigo_digitado = int(input("Código do produto: "))
    buscar_produtos()
    adicionar_preço()
    adicionar_nomes()
    adicionar_algo = input("Deseja adicionar algo mais? ")
else:
    print(nome_produtos_comprados)
    print(f"Valor total a pagar: {sum(preço_produtos_comprados)}")