import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def calcular_similaridade(self, matriz_avaliacoes):
        
        if matriz_avaliacoes.size == 0 or len(matriz_avaliacoes) < 2:
            return np.array([])
        try:
            return cosine_similarity(matriz_avaliacoes)
        except Exception as e:
            print(f"Erro ao calcular similaridade: {e}")
            return np.array([])

    def recomendar(self, user, max_recomendacoes=10):
        """
        
        """
        dados, itens, usuarios, matriz_avaliacoes = self.data_manager.get_dados()

        if user not in usuarios:
            print(f"Usuário {user} não encontrado")
            return []

        if len(usuarios) < 2:
            print("Sistema precisa de pelo menos 2 usuários para gerar recomendações")
            return []

        if matriz_avaliacoes.size == 0:
            print("Nenhuma avaliação encontrada")
            return []

        try:
           
            index_usuario = usuarios.index(user)
            avaliacoes_usuario_atual = matriz_avaliacoes[index_usuario]
            
           
            if np.sum(avaliacoes_usuario_atual) == 0:
                print(f"Usuário {user} não tem avaliações. Recomendando itens populares...")
                return self.recomendar_populares(max_recomendacoes)
            
            
            similaridade = self.calcular_similaridade(matriz_avaliacoes)
            if similaridade.size == 0:
                print("Não foi possível calcular similaridade")
                return self.recomendar_populares(max_recomendacoes)

            similaridade_usuario = similaridade[index_usuario]

            
            usuarios_similares = np.argsort(similaridade_usuario)[::-1][1:]

            itens_recomendados = []
            itens_ja_recomendados = set()

           
            for usuario_similar in usuarios_similares:
                
                if matriz_avaliacoes[usuario_similar].sum() == 0:
                    continue
                
                
                if similaridade_usuario[usuario_similar] <= 0:
                    continue

                for i, (tipo, item) in enumerate(itens):
                    
                    if (i < len(matriz_avaliacoes[usuario_similar]) and
                        i < len(matriz_avaliacoes[index_usuario]) and
                        matriz_avaliacoes[usuario_similar][i] >= 3 and 
                        item not in itens_ja_recomendados and
                        matriz_avaliacoes[index_usuario][i] == 0):

                       
                        score = similaridade_usuario[usuario_similar] * matriz_avaliacoes[usuario_similar][i]

                        itens_recomendados.append({
                            'item': f"{tipo}: {item}",
                            'score': score,
                            'nota': matriz_avaliacoes[usuario_similar][i],
                            'usuario_similar': usuarios[usuario_similar],
                            'tipo': tipo
                        })
                        itens_ja_recomendados.add(item)

                        if len(itens_recomendados) >= max_recomendacoes:
                            break

                if len(itens_recomendados) >= max_recomendacoes:
                    break

            
            if len(itens_recomendados) < 3:
                populares = self.recomendar_populares(max_recomendacoes - len(itens_recomendados))
                for popular in populares:
                    if popular not in [item['item'] for item in itens_recomendados]:
                        itens_recomendados.append({
                            'item': popular,
                            'score': 2.0,
                            'nota': 4,
                            'usuario_similar': 'Sistema',
                            'tipo': popular.split(':')[0]
                        })

            
            itens_recomendados.sort(key=lambda x: x['score'], reverse=True)

            
            resultado = [item['item'] for item in itens_recomendados]
            print(f"Geradas {len(resultado)} recomendações para {user}")
            return resultado

        except Exception as e:
            print(f"Erro na geração de recomendações: {e}")
            return self.recomendar_populares(max_recomendacoes)

    def recomendar_populares(self, max_recomendacoes=10):
        
        dados, itens, usuarios, matriz_avaliacoes = self.data_manager.get_dados()
        
       
        popularidade_itens = []
        
        for i, (tipo, nome) in enumerate(itens):
            if matriz_avaliacoes.size > 0:
                
                avaliacoes_item = matriz_avaliacoes[:, i] if i < matriz_avaliacoes.shape[1] else np.array([])
                avaliacoes_positivas = avaliacoes_item[avaliacoes_item >= 3]
                
                if len(avaliacoes_positivas) > 0:
                    popularidade = len(avaliacoes_positivas) * np.mean(avaliacoes_positivas)
                else:
                    popularidade = 0
            else:
                
                popularidade = len(itens) - i
            
            popularidade_itens.append({
                'item': f"{tipo}: {nome}",
                'popularidade': popularidade
            })
        
       
        popularidade_itens.sort(key=lambda x: x['popularidade'], reverse=True)
        
        
        resultado = [item['item'] for item in popularidade_itens[:max_recomendacoes]]
        print(f"Recomendações populares: {len(resultado)} itens")
        return resultado

    def obter_recomendacoes_detalhadas(self, user, max_recomendacoes=10):
        
        dados, itens, usuarios, matriz_avaliacoes = self.data_manager.get_dados()

        if user not in usuarios or len(usuarios) < 2:
            return []

        if matriz_avaliacoes.size == 0 or len(matriz_avaliacoes) < 2:
            return []

        try:
            similaridade = self.calcular_similaridade(matriz_avaliacoes)
            if similaridade.size == 0:
                return []

            index_usuario = usuarios.index(user)
            similaridade_usuario = similaridade[index_usuario]
            usuarios_similares = np.argsort(similaridade_usuario)[::-1][1:]

            itens_recomendados = []
            itens_ja_recomendados = set()

            for usuario_similar in usuarios_similares:
                if (matriz_avaliacoes[usuario_similar].sum() == 0 or 
                    similaridade_usuario[usuario_similar] <= 0):
                    continue

                for i, (tipo, item) in enumerate(itens):
                    if (i < len(matriz_avaliacoes[usuario_similar]) and
                        i < len(matriz_avaliacoes[index_usuario]) and
                        matriz_avaliacoes[usuario_similar][i] > 3 and 
                        item not in itens_ja_recomendados and
                        matriz_avaliacoes[index_usuario][i] == 0):

                        score = similaridade_usuario[usuario_similar] * matriz_avaliacoes[usuario_similar][i]

                        itens_recomendados.append({
                            'item': f"{tipo}: {item}",
                            'score': score,
                            'nota': matriz_avaliacoes[usuario_similar][i],
                            'usuario_similar': usuarios[usuario_similar],
                            'similaridade': similaridade_usuario[usuario_similar],
                            'tipo': tipo
                        })
                        itens_ja_recomendados.add(item)

                        if len(itens_recomendados) >= max_recomendacoes:
                            break

                if len(itens_recomendados) >= max_recomendacoes:
                    break

            return sorted(itens_recomendados, key=lambda x: x['score'], reverse=True)

        except Exception as e:
            print(f"Erro na análise detalhada: {e}")
            return []