
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui import main
    
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"Erro de importação: {e}")
    print("Verifique se todos os arquivos estão no mesmo diretório.")
except Exception as e:
    print(f"Erro ao executar o programa: {e}")
    input("Pressione Enter para sair...")
