import numpy as np
import json
import os

class DataManager:
    def __init__(self):
        self.dados = {}
        self.dados_file = 'dados_usuarios.json'

        self.itens = [
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
            ('Produto', 'Caixa de Som Bluetooth')
        ]

        self.usuarios = []
        self.matriz_avaliacoes = np.array([])

        
        self.carregar_dados()

    def get_dados(self):
        if self.usuarios:
            
            for usuario in self.usuarios:
                if usuario in self.dados:
                    while len(self.dados[usuario]) < len(self.itens):
                        self.dados[usuario].append(0)
                    
                    self.dados[usuario] = self.dados[usuario][:len(self.itens)]
                else:
                    self.dados[usuario] = [0] * len(self.itens)

            
            matriz_data = []
            for usuario in self.usuarios:
                user_data = self.dados[usuario][:len(self.itens)]
               
                while len(user_data) < len(self.itens):
                    user_data.append(0)
                matriz_data.append(user_data)

            if matriz_data:
                self.matriz_avaliacoes = np.array(matriz_data)
            else:
                self.matriz_avaliacoes = np.array([]).reshape(0, len(self.itens))
        else:
            self.matriz_avaliacoes = np.array([]).reshape(0, len(self.itens))

        return self.dados, self.itens, self.usuarios, self.matriz_avaliacoes

    def adicionar_item(self, tipo, nome_item):
        
        for t, n in self.itens:
            if t == tipo and n == nome_item:
                return False 

        self.itens.append((tipo, nome_item))

        
        for user in self.usuarios:
            if user in self.dados:
                
                while len(self.dados[user]) < len(self.itens):
                    self.dados[user].append(0)
            else:
                self.dados[user] = [0] * len(self.itens)

        
        if self.usuarios:
            matriz_data = []
            for usuario in self.usuarios:
                
                while len(self.dados[usuario]) < len(self.itens):
                    self.dados[usuario].append(0)
                matriz_data.append(self.dados[usuario])
                try:
                    self.matriz_avaliacoes = np.array(matriz_data, dtype=np.float64)
                except ValueError:
                    self.matriz_avaliacoes = np.zeros((len(self.usuarios), len(self.itens)), dtype=np.float64)
            else:
                self.matriz_avaliacoes = np.zeros((0, len(self.itens)), dtype=np.float64)

        
        sucesso = self.salvar_dados()
        print(f"Item adicionado: {tipo} - {nome_item}, Total de itens: {len(self.itens)}")
        return sucesso

    def adicionar_usuario(self, nome_usuario):
        if nome_usuario not in self.usuarios:
            self.usuarios.append(nome_usuario)
            self.dados[nome_usuario] = [0] * len(self.itens)

            
            if self.usuarios:
                matriz_data = []
                for usuario in self.usuarios:
                   
                    while len(self.dados[usuario]) < len(self.itens):
                        self.dados[usuario].append(0)
                    matriz_data.append(self.dados[usuario])
                try:
                    self.matriz_avaliacoes = np.array(matriz_data, dtype=np.float64)
                except ValueError:
                    self.matriz_avaliacoes = np.zeros((len(self.usuarios), len(self.itens)), dtype=np.float64)
            else:
                self.matriz_avaliacoes = np.zeros((0, len(self.itens)), dtype=np.float64)

            self.salvar_dados()  
            return True
        return False

    def avaliar_item(self, usuario, item_index, nota):
        try:
            if usuario in self.dados and 0 <= item_index < len(self.itens) and 1 <= nota <= 5:
                
                while len(self.dados[usuario]) < len(self.itens):
                    self.dados[usuario].append(0)

                self.dados[usuario][item_index] = nota

                
                if self.usuarios:
                    matriz_data = []
                    for usuario in self.usuarios:
                        
                        while len(self.dados[usuario]) < len(self.itens):
                            self.dados[usuario].append(0)
                        matriz_data.append(self.dados[usuario])
                    try:
                        self.matriz_avaliacoes = np.array(matriz_data, dtype=np.float64)
                    except ValueError:
                        self.matriz_avaliacoes = np.zeros((len(self.usuarios), len(self.itens)), dtype=np.float64)
                else:
                    self.matriz_avaliacoes = np.zeros((0, len(self.itens)), dtype=np.float64)

                self.salvar_dados()  
                return True
            return False
        except Exception as e:
            print(f"Erro na avaliação: {e}")
            return False

    def salvar_dados(self):
        
        try:
            dados_para_salvar = {
                'usuarios': self.usuarios,
                'dados_avaliacoes': self.dados,
                'itens_adicionados': []
            }

            
            if len(self.itens) > 82:
                dados_para_salvar['itens_adicionados'] = self.itens[82:]

            with open(self.dados_file, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, ensure_ascii=False, indent=2)

            return True
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
            return False

    def carregar_dados(self):
       
        try:
            if os.path.exists(self.dados_file):
                with open(self.dados_file, 'r', encoding='utf-8') as f:
                    dados_salvos = json.load(f)

                
                self.usuarios = dados_salvos.get('usuarios', [])

                
                self.dados = dados_salvos.get('dados_avaliacoes', {})

                
                itens_adicionados = dados_salvos.get('itens_adicionados', [])
                if itens_adicionados:
                    self.itens.extend(itens_adicionados)

               
                if self.usuarios:
                    
                    for usuario in self.usuarios:
                        if usuario in self.dados:
                            while len(self.dados[usuario]) < len(self.itens):
                                self.dados[usuario].append(0)
                        else:
                            self.dados[usuario] = [0] * len(self.itens)

                    self.matriz_avaliacoes = np.array(list(self.dados.values()))

                print(f"Dados carregados: {len(self.usuarios)} usuários, {len(self.itens)} itens")
                return True
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False