print("Lista de contatos:")

lista_de_nomes = ["João" , "Caio" , "Jubileu"]
Escolha = 5 
while Escolha != 0:
    Escolha = int(input("O que você quer fazer? \n [1] - Cadastrar pessoas \n [2] - Listar pessoas \n [3] - Excluir_pessoas \n [0] - Sair"))
    
    if Escolha == 1:
        Adicionamento = input("Qual contato você quer adicionar?")
        lista_de_nomes.append(Adicionamento)
        print("Contato adicionado com sucesso!")       
    elif Escolha == 2:
        print(lista_de_nomes) 
    elif Escolha == 3:
        Removimento = input("Qual contato você quer remover?")
        lista_de_nomes.remove(Removimento)
        print("Contato removido com sucesso!")
    elif Escolha == 0:
        print("Fechado com Sucesso!")
