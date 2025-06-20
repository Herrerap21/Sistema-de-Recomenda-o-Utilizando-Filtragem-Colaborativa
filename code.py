import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def inicializar_dados():
    
    dados = {
        'User1': [5, 4, 0, 0, 3, 0, 4, 5, 0, 0, 4, 5, 3, 0, 5, 4, 3, 2, 0, 5, 5, 0, 0, 4, 3, 0, 5, 4, 3, 5, 4, 0, 0, 5, 3, 4, 5, 4, 3, 2],  # Filmes, Livros, Produtos
        'User2': [4, 0, 0, 2, 0, 1, 3, 0, 5, 0, 5, 3, 4, 5, 2, 3, 4, 5, 2, 4, 5, 3, 2, 3, 1, 5, 4, 2, 0, 4, 3, 5, 3, 4, 5, 2, 0, 4, 5, 3],
        'User3': [0, 0, 5, 4, 0, 2, 4, 3, 5, 4, 5, 3, 5, 0, 3, 4, 5, 5, 4, 5, 4, 3, 2, 4, 0, 5, 5, 4, 4, 5, 5, 4, 5, 3, 4, 5, 4, 5, 4, 5],
        'User4': [0, 3, 4, 0, 0, 5, 5, 4, 0, 3, 3, 4, 5, 0, 4, 3, 4, 4, 2, 5, 4, 3, 4, 2, 5, 0, 4, 3, 5, 4, 3, 2, 5, 4, 3, 3, 4, 5, 3, 2],
        'User5': [2, 0, 3, 5, 0, 0, 5, 4, 2, 3, 3, 4, 5, 2, 3, 5, 2, 3, 5, 4, 5, 3, 2, 4, 0, 2, 3, 5, 2, 3, 5, 4, 4, 3, 5, 5, 2, 4, 3, 3]
    }
    
    itens = [
    
        ('Filme', 'O Homem Invisível'),
        ('Filme', 'Vingadores: Ultimato'),
        ('Filme', 'Star Wars: A Ascensão Skywalker'),
        ('Filme', 'O Rei Leão'),
        ('Filme', 'O Poderoso Chefão'),
        ('Filme', 'Matrix'),
        ('Filme', 'Jurassic Park'),
        ('Filme', 'O Senhor dos Anéis: O Retorno do Rei'),
        ('Filme', 'Titanic'),
        ('Filme', 'A Origem'),
        ('Filme', 'Parasita'),
        ('Filme', 'Gladiador'),
        ('Filme', 'Inception'),
        ('Filme', 'A Culpa é das Estrelas'),
        ('Filme', 'O Lobo de Wall Street'),
        ('Filme', 'John Wick'),
        ('Filme', 'Jurassic World'),
        ('Filme', 'A Bela e a Fera'),
        ('Filme', 'Mad Max: Estrada da Fúria'),
        ('Filme', 'Avatar'),
        ('Filme', 'Batman: O Cavaleiro das Trevas'),
        ('Filme', 'Spider-Man: No Way Home'),
        ('Filme', 'Frozen 2'),
        ('Filme', 'Logan'),
        ('Filme', 'Dunkirk'),
        ('Filme', 'Interstellar'),
        ('Filme', 'O Regresso'),
        ('Filme', 'O Grande Lebowski'),
        ('Filme', 'Deadpool'),
        ('Filme', 'Pulp Fiction'),

        ('Livro', 'O Hobbit'),
        ('Livro', '1984'),
        ('Livro', 'Dom Quixote'),
        ('Livro', 'Harry Potter e a Pedra Filosofal'),
        ('Livro', 'O Senhor dos Anéis: A Sociedade do Anel'),
        ('Livro', 'A Guerra dos Tronos'),
        ('Livro', 'O Código Da Vinci'),
        ('Livro', 'O Pequeno Príncipe'),
        ('Livro', 'Orgulho e Preconceito'),
        ('Livro', 'O Alquimista'),
        ('Livro', 'Cem Anos de Solidão'),
        ('Livro', 'O Nome do Vento'),
        ('Livro', 'O Diário de Anne Frank'),
        ('Livro', 'O Senhor dos Anéis: As Duas Torres'),
        ('Livro', 'O Mundo de Sofia'),
        ('Livro', 'Matar um Rouxinol'),
        ('Livro', 'O Guia do Mochileiro das Galáxias'),
        ('Livro', 'As Aventuras de Sherlock Holmes'),
        ('Livro', 'O Caçador de Pipas'), 
        ('Livro', 'A Revolução dos Bichos'),
        ('Livro', 'O Ladrão de Raios'),
        ('Livro', 'O Cemitério'),
        ('Livro', 'A Menina que Roubava Livros'),
        ('Livro', 'A Mulher na Janela'),
        ('Livro', 'Os Homens que Não Amavam as Mulheres'),
        ('Livro', 'O Símbolo Perdido'),
        ('Livro', 'A Culpa é das Estrelas'),
        ('Livro', 'O Príncipe'),
        ('Livro', 'A Arte da Guerra'),

        ('Produto', 'Smartphone Galaxy S21'),
        ('Produto', 'Cafeteira Expresso'),
        ('Produto', 'Fone de Ouvido Bluetooth'),
        ('Produto', 'Cadeira Gamer Ergonômica'),
        ('Produto', 'Relógio Inteligente'),
        ('Produto', 'Câmera DSLR Canon EOS'),
        ('Produto', 'Laptop Dell XPS 13'),
        ('Produto', 'Tablet iPad Pro'),
        ('Produto', 'Air Fryer'),
        ('Produto', 'Smartwatch Garmin'),
        ('Produto', 'Headset de Jogo'),
        ('Produto', 'Controle de Xbox'),
        ('Produto', 'Computador de Mesa'),
        ('Produto', 'TV 4K LG'),
        ('Produto', 'Assistente Virtual Alexa'),
        ('Produto', 'Mini Geladeira Portátil'),
        ('Produto', 'Projetor para Home Theater'),
        ('Produto', 'Console PlayStation 5'),
        ('Produto', 'Console Nintendo Switch'),
        ('Produto', 'Mouse Gamer Logitech'),
        ('Produto', 'Teclado Mecânico Razer'),
        ('Produto', 'Monitor Curvo Samsung'),
        ('Produto', 'Soundbar JBL'),
        ('Produto', 'Caixa de Som Bluetooth'),
        ('Produto', 'Micro-ondas Panasonic'),
        ('Produto', 'Secador de Cabelo Philips'),
        ('Produto', 'Lâmpada Inteligente Wi-Fi'),
        ('Produto', 'Batedeira KitchenAid'),
        ('Produto', 'Máquina de Lavar LG'),
        ('Produto', 'Aspirador de Pó Robô'),
        ('Produto', 'Fritadeira Elétrica')

    ]
    
    usuarios = ['User1', 'User2', 'User3', 'User4', 'User5']
    
    matriz_avaliacoes = np.array(list(dados.values()))
    
    return dados, itens, usuarios, matriz_avaliacoes

def calcular_similaridade(matriz_avaliacoes):
    return cosine_similarity(matriz_avaliacoes)

def recomendar(user, usuarios, similaridade, itens, matriz_avaliacoes):
    index_usuario = usuarios.index(user)
    similaridade_usuario = similaridade[index_usuario]
    usuarios_similares = np.argsort(similaridade_usuario)[::-1][1:]  
    
    itens_recomendados = []

    for usuario_similar in usuarios_similares:
        for i, (tipo, item) in enumerate(itens):
            if matriz_avaliacoes[usuario_similar][i] > 0 and item not in itens_recomendados:
                itens_recomendados.append(f"{tipo}: {item}")

    return itens_recomendados

def adicionar_item(itens, dados, matriz_avaliacoes):
    tipo = input("Digite o tipo do item (Filme, Livro, Produto): ")
    nome_item = input(f"Digite o nome do {tipo}: ")
    itens.append((tipo, nome_item))
    
    nova_avaliacao = [0] * len(itens)
    dados['User1'].append(0)  
    matriz_avaliacoes = np.array(list(dados.values()))
    
    print(f"{tipo} '{nome_item}' adicionado com sucesso!")
    return itens, dados, matriz_avaliacoes

def menu():
    dados, itens, usuarios, matriz_avaliacoes = inicializar_dados()
    similaridade = calcular_similaridade(matriz_avaliacoes)

    while True:
        print("\nSistema de Recomendação")
        print("1. Exibir recomendações para um usuário")
        print("2. Adicionar novo item (filme, livro, produto)")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            user = input("Digite o nome do usuário para recomendações (User1, User2, etc.): ")
            if user in usuarios:
                recomendacoes = recomendar(user, usuarios, similaridade, itens, matriz_avaliacoes)
                print(f"\nRecomendações para {user}: {recomendacoes}")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == '2':
            itens, dados, matriz_avaliacoes = adicionar_item(itens, dados, matriz_avaliacoes)
        
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def iniciar_sistema():
    menu()

iniciar_sistema()
