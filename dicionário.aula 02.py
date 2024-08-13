# Função para coletar e exibir informações de um contato
def coletar_informacoes_contato():
    # Cria um dicionário vazio para armazenar as informações do contato
    contato = {}
    
    # Solicita ao usuário para inserir o nome do contato
    nome = input("Digite o nome do contato: ")
    contato['nome'] = nome
    
    # Solicita ao usuário para inserir o número de telefone
    telefone = input("Digite o número de telefone do contato: ")
    contato['telefone'] = telefone
    
    # Solicita ao usuário para inserir o endereço de email
    email = input("Digite o endereço de email do contato: ")
    contato['email'] = email
    
    # Exibe o conteúdo do dicionário
    print("\nInformações do Contato:")
    print(f"Nome: {contato['nome']}")
    print(f"Telefone: {contato['telefone']}")
    print(f"Email: {contato['email']}")

# Chama a função para executar o programa
coletar_informacoes_contato()
